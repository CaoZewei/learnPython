from die import Die
import pygal

die = Die()

results =[]
for rolls in range(1000):
    result = die.roll()
    results.append(result)
frequencies=[]
for v in range(1,die.num_sides+1):
    frequency =results.count(v)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "sdbnuaf"
hist.x_labels=['1','2','3','4','5','6']
hist.x_title ="result"
hist.y_title="frequencies"
hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')
print(frequencies)