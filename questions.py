import openai

API_key = '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'
openai.api_key = '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'
role = "You are a scientist with expertise in chemical engineering, physical experiments, and data science."
context = """These experiments are Combustion (Pyrolysis) experiments in presence of oxygen for biomass to biochar formation in a newly designed small-sized reactor. A hopper is used for inputting biomass, an auger rotates at a certain speed to carry the biomass in the reactor where it is burnt. Volatiles go from chimney above, and output biochar goes from the other end of the auger. Thermocouples measure the temperature at different places. Primary blowers provide air (hence oxygen) to the reactor zone, and secondary blowers remove volatiles through the chimney. The objective is to gain a complete understanding of the underlying combustion process and machine design by testing different hypotheses.\n"""
order = "Answer the questions given the data in the hot_test"
hot_test = """
Hot Test # 64 - 4/4/22  
Personnel: Austin and Kevin 
Objective: 
To repeat Hot Test #63 but with the rectangular cross section replaced with a circular cross section. The hypothesis is that given the much tighter auger fit with the circular cross section, we might replicate Indian MiniTorr’s observation that the auger/motor is having issues conveying raw rice husks past the rectangular -> circular transition.  
Setting: 
Motor RPM began at 6, then we increased to 10. When we noticed motor was struggling, we lowered it to 6.  
Results: 
After about an hour of running, the motor started struggling. Reducing the RPM didn’t help. Eventually when we opened the cover, we found the rectangular-to-circular transition jam-packed with raw biomass. This seems to conclusively demonstrate that the Indian MiniTorr jamming is likely caused by the tight clearance between the reactor inner wall and the flights of the auger.  Other Observations 
Input feedrate was around 29 kg/h.  
Initially we had smoke leaking from the hopper and the cracks which was unusual for a primary blower position so high up the reactor. A closer examination revealed that the damper of the chimney was on (also for the previous hot test)!! After the damper was removed, the smoke from hopper and cracks disappeared. Ash out of the chimney was severe but came in episodes.  
Later on the motor got stuck repeatedly, Austin noticed that the motor driver wires got hot (not sure if it’s due to overcurrent or a poorly connected junction). As he attempted to fix this, the PLC went haywire – all blowers went high and the motor stopped working. We had to power-cycle through the PLC. When we regained control, the motor was still periodically stuck.   
Next Steps 
Repeat the same test but with primary blower at a much lower position. If the reaction and volumetric reduction can start earlier in the reactor, this could prevent the jamming at the rectangular-circular transition.  
Also start searching for some rice straws to repeat the same experiment as today.

Hot Test # 114 30/06/23
People: Arthur, Colson, Josh and Dylan
Hypothesis: To see if the mega chimney reduced the amount of embers and ash coming out of the top of the chimney. This is compared against the previous test (#113), which used the small chimney.
Settings: Primary blowers at S10. Variable pitch auger used, running at 6rpm for most of the test. Mega Chimney used without mesh. Prototype set up at 30° with small barrel being used.
All blowers except D were giving a reading
Labjack fixed since last week's test, was not plugged in so did not record
Feedstock: Cloverdale woodchips
Summary: To start the test, we packed the chips into the flights by hand to prevent the auger from jamming, which it seemed to do. When the reaction was initially lit, there was substantial ash for a few minutes, which then decreased. There was no smoke throughout the test. The embers / ashes acted the same as they did in the small chimney, in the aspect that there was a baseline of ash, and every once and awhile there would be a large plume of ash. We did notice that there was a similar amount of ash, but the ash was only compromised of small flakes, unlike the small chimney, which had large flakes and chunks of embers. We only got a few burns each, which was a substantial decrease from the small chimney. We each only got a hole or two in our shirts, which was also a substantial decrease from the small chimney. The auger tripped and jammed multiple times, and we hypothesize that this is due to a larger gap at the back end of the hopper allowing woodchips to get jammed into it. This larger gap was due to us having to slightly angle the hopper forward to make it fit with the mega chimney. To undo the jamming, we moved the auger forward and backward a few times. We also almost had a few hopper fires, which usually occurred when we were trying to unjam the hopper. When the fire got close to the hopper, we moved the auger forward until we couldn’t see flames in the flight in front of the hopper. We also tested different blower settings and concluded that increasing the primary blowers created more ash, and increasing the secondary blowers made the ash go farther. At the end of the test, a piece of ember got stuck in the output curtain, which caught fire, and burnt a hole through it. The hopper also caught fire, but there were only a few woodchips left in it, so we let it burn and be pushed forward into the reactor. We put this out by dumping water on the curtain + biochar barrel, which put it out. Woodchip bridging occurred in the hopper, but we broke them by hand quickly. We found that the blowers pulsed a few times but were otherwise consistent.
Suggestions: Blower settings had a small effect on the amount of embers, but even with both at their lowest there was still ashes coming out. This makes us believe that we should experiment with other solutions than chimney size, as even with this chimney, which was the largest, there was still ash coming out. We also need to buy a new output curtain that is longer than the current curtain, so we can tension the curtain down so there are no pockets for an ember to get caught in. We need to fix the last blower
PROPRIETARY AND CONFIDENTIAL. PLEASE DO NOT DISTRIBUTE
WITH PERMISSION.
and figure out how to reduce the amount of jamming in the auger. We also found that the woodchips would clump in one corner, which might be a jamming point that we will have to fix.
Fire

Hot Test # 113 28/06/23
People: Kevin, Arthur, Colson, Jayson, Josh and Dylan
Hypothesis: To test whether larger pitch auger will reduce jamming. We also had to run reactor long enough for VIP’s to see the hot test.
Settings: Primary blowers at S10. Variable pitch auger used, running at 6rpm for most of the test. Small chimney mounted with no mesh. Prototype set up at 30° with small barrel being used.
All blowers except D were giving a reading
Labjack fixed since last weeks test
Feedstock: Cloverdale woodchips
Summary: The goal for today’s hot test was to test the new variable pitch auger. The same feedstock and reactor setup was used as test #110. Overall variable pitch auger seems to reduce the number of times the motor trips. However, the motor still tripped twice during the test, but ran much more smoothly when the reactor got hot (tripped once). The auger was reversed a few times to clear up the jamming. At the start of the test, the auger was turned on and off to avoid conveying material too quickly. Eventually, the auger was run continuously as material did not seem to move too quickly and reaction was sustaining well. We noticed that the auger would jam more when the hopper was empty.
Hopper worked well but we noticed some bridging. Lots of embers and ash during the test. This is most likely because of the small cross-sectional area of the chimney. The woodchips were quite dry, which may have contributed to the issue. Secondary blower speed was increased, and primary blower speed was reduced. Could not conclude whether this helped.
Multiple times during the test, flames were noticed out of the top of the chimney. The secondary blower rpm was increased to counteract this.
PROPRIETARY AND CONFIDENTIAL. PLEASE DO NOT DISTRIBUTE
WITH PERMISSION.
PROPRIETARY AND CONFIDENTIAL. PLEASE DO NOT DISTRIBUTE
WITH PERMISSION.
Suggestions: The test will be repeated with the same conditions and feedstock but with a larger chimney. The goal will be to find the ideal chimney area that reduces the amount of ash and embers but is still easy to handle when taking on and off. If problem persists, other solutions will be looked into such as installing a mesh.
Blower shown on image above will need to be tested. RPM seems to ramp up and down, and reading does not show. Possibly in need of new connector or to be replaced.
"""
question1 = """What are the top reasons, potential solutions from experiments and solutions in literature for 
1. reactor stopping in the initial stages
2. lowering of temperature and need for re-ignition
3. auger motor tripping/ jamming (important)
4. bridging issues /biomass getting stuck issues in the hopper
5. smoke coming out of the reactor chimney (important)
6. smoke coming out of the hopper
7. poor quality output char"""
question2 = """What strong correlations exist in the data between blowers, auger, temperature, input, output."""
question3 = """Which reactor changes have led to the most improvements"""
question4 = """What are the optimal reactor settings and input settings and why?"""
question5 = """What should I do?
1. To increase or decrease temperature
2. To reduce probability of tripping/ auger jamming
3. To increase output yield and char quality
4. To maintain steady-state for longer periods of time"""

question6 = """What are the effects of:
increasing primary or secondary blower speed,
increasing auger speed,
increasing temperature,
rice vs wood-based inputs"""


# Generate answers for the questions
response = openai.Completion.create(
        engine='text-davinci-003',
        prompt = role + "\n" + context + "\n" + order + hot_test+ question1 +"\n" + question2+ "\n" + question3 +"\n" + question4 +"\n" + question5 +"\n" + question6,
        max_tokens=1800,
        temperature=0.7
    )

# Get the generated completion
output = response.choices[0].text.strip()

# Print the output
print(output)