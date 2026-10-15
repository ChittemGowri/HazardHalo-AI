"""Deterministic normalized polygon occupancy decision engine."""
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

@dataclass(frozen=True)
class Detection:
    label: str; confidence: float; bbox: tuple[float, float, float, float]
    timestamp: datetime; source: str = "unknown"; track_id: Optional[str] = None

@dataclass(frozen=True)
class ZoneConfig:
    name: str; polygon: tuple[tuple[float, float], ...]; confidence_threshold: float = .5
    entry_confirmation_seconds: float = 1.; clear_confirmation_seconds: float = 1.; alert_cooldown_seconds: float = 30.

def point_in_polygon(point, polygon):
    x, y = point
    # Boundary is inside, so operators can safely draw inclusive boundaries.
    for (ax, ay), (bx, by) in zip(polygon, polygon[1:] + polygon[:1]):
        cross = (x-ax)*(by-ay) - (y-ay)*(bx-ax)
        if abs(cross) < 1e-9 and min(ax,bx)-1e-9 <= x <= max(ax,bx)+1e-9 and min(ay,by)-1e-9 <= y <= max(ay,by)+1e-9: return True
    inside = False
    for (ax, ay), (bx, by) in zip(polygon, polygon[1:] + polygon[:1]):
        if (ay > y) != (by > y) and x < (bx-ax)*(y-ay)/(by-ay)+ax: inside = not inside
    return inside

class ZoneEngine:
    def __init__(self, config: ZoneConfig):
        if len(config.polygon) < 3: raise ValueError("polygon needs at least three points")
        self.config, self.alerted, self.present_since, self.absent_since, self.last_alert = config, False, None, None, None
    def _occupancy(self, detections):
        for d in detections:
            if d.label.lower() != "person" or not 0 <= d.confidence <= 1 or d.confidence < self.config.confidence_threshold: continue
            if len(d.bbox) != 4: continue
            x, y, w, h = d.bbox; px, py = x + w/2, y + h
            if all(0 <= q <= 1 for q in (x,y,w,h,px,py)) and point_in_polygon((px,py), self.config.polygon): return True
        return False
    def evaluate(self, detections, now=None):
        now = now or datetime.now(timezone.utc); occupied = self._occupancy(detections); events=[]
        if occupied:
            self.absent_since = None; self.present_since = self.present_since or now
            eligible = (now-self.present_since).total_seconds() >= self.config.entry_confirmation_seconds
            cooldown = not self.last_alert or (now-self.last_alert).total_seconds() >= self.config.alert_cooldown_seconds
            if not self.alerted and eligible and cooldown:
                self.alerted=True; self.last_alert=now; events.append("PERSON_IN_ZONE")
        else:
            self.present_since = None; self.absent_since = self.absent_since or now
            if self.alerted and (now-self.absent_since).total_seconds() >= self.config.clear_confirmation_seconds:
                self.alerted=False; events.append("ZONE_CLEARED")
        return events
