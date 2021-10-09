from time import sleep

def progress(time):
  length = 10
  placeholder = '----------'
  output = ''
  min, sec = timer(-1, time, length)
  print(f'sleeping progress:', placeholder + f' {min}m {sec}s (0%)', end='\r')
  for ii in range(length):
    sleep(time//length)
    output = '#' + output[0:ii] + placeholder[ii:length-1]
    min, sec = timer(ii, time, length)
    output += f' {min}m {sec}s ({(ii+1)*length}%) '
    print(f'sleeping progress:', output, end='\r')
  print('')

def timer(it, full_time, division_rate):
  minutes_counter = (full_time - ((it+1) * full_time//division_rate))//60
  seconds_counter = (full_time - ((it+1) * full_time//division_rate))%60
  return minutes_counter, seconds_counter

