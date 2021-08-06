from die import Die
import pygal

die1 = Die()
die2 = Die()

results =[]
for rolls in range(1000):
    result = die1.roll()+die2.roll()
    results.append(result)

frequencies=[]
max_num =die1.num_sides+die2.num_sides
for v in range(1,max_num+1):
    frequency =results.count(v)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "result of roll 2 D6 dice 1000 times"
hist.x_labels=['1','2','3','4','5','6']
hist.x_title ="result"
hist.y_title="frequencies"
hist.add('D6+D6',frequencies)
hist.render_to_file('dice_visual.svg')
print(frequencies)