def moon_phase(phase):
  if phase == 0 or phase == 360:
    return 'New Moon'
  elif phase > 0 and phase < 90:
    return 'Waxing Crescent'
  elif phase == 90:
    return 'First Quarter'
  elif phase > 90 and phase < 180:
    return 'Waxing Gibbous'
  elif phase == 180:
    return 'Full Moon'
  elif phase > 180 and phase < 270:
    return 'Waning Gibbous'
  elif phase == 270:
    return 'Last Quarter'
  elif phase > 270 and phase < 360:
    return 'Waning Gibbous'
  else:
    return 'Invalid moon phase'

print(moon_phase(180))

