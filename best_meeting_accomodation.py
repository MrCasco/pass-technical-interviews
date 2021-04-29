"""
input:  slotsA = [[10, 15],  [60, 120], [140, 210]]    n = 100000
slotsB = [[0, 15],   [40, 20]]                         m = 2
dur = 8
"""

def meeting_planner(slotsA, slotsB, dur):
  a, b = 0, 0
  while a < len(slotsA) and b < len(slotsB):
    end_time = min(slotsA[a][1], slotsB[b][1])
    start_time = max(slotsA[a][0], slotsB[b][0])
    window = end_time-start_time
    if window < dur:
      if slotsB[b][1] < slotsA[a][1]:
        b += 1
      else:
        a += 1
    else:
      return [start_time, start_time+dur]
  return []
