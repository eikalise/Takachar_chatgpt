import openai

API_key = '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'
openai.api_key = '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'
role = "You are a scientist with expertise in chemical engineering, physical experiments, and data science."
context = """These experiments are Combustion (Pyrolysis) experiments in presence of oxygen for biomass to biochar formation in a newly designed small-sized reactor. A hopper is used for inputting biomass, an auger rotates at a certain speed to carry the biomass in the reactor where it is burnt. Volatiles go from chimney above, and output biochar goes from the other end of the auger. Thermocouples measure the temperature at different places. Primary blowers provide air (hence oxygen) to the reactor zone, and secondary blowers remove volatiles through the chimney. The objective is to gain a complete understanding of the underlying combustion process and machine design by testing different hypotheses.\n"""
questions = [
    "What are the top reasons, potential solutions from experiments, and solutions in literature for reactor stopping in the initial stages?",
    "What are the potential solutions and literature recommendations for lowering of temperature and the need for re-ignition?",
    "What are the common causes and experimental remedies for auger motor tripping or jamming?",
    "How can the bridging issues and biomass getting stuck in the hopper be resolved?",
    "What are the possible causes and solutions for smoke coming out of the reactor chimney?",
    "How can the issue of smoke coming out of the hopper be addressed?",
    "What are the methods to improve the quality of the output char?",
    "What strong correlations exist in the data between blowers, auger, temperature, input, and output?",
    "Which changes in the reactor design have led to the most significant improvements?",
    "What are the optimal reactor settings and input settings, and why?",
    "What actions should be taken to increase or decrease the temperature?",
    "How can the probability of auger tripping or jamming be reduced?",
    "What measures can be taken to increase the output yield and improve char quality?",
    "How can steady-state operation for longer periods be maintained?",
    "What are the effects of increasing the primary or secondary blower speed?",
    "How does the auger speed impact the process?",
    "What is the influence of temperature on the combustion process?",
    "What are the differences in performance between rice-based and wood-based inputs?"
]
hot_test = """Summarize the following hot test into a table. Only include the following columns: Hot Test #, data, People, objective, hypothesis, test results, observation/insights,  suggestions, quality score. To determine quality score between 0 to 1, 0 is completely fail, while 1 means no smoke, no tripping, short reaction time, good output char quality, no reignition, no embers :

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

Also start searching for some rice straws to repeat the same experiment as today."""


# Generate completion using the prompt
response = openai.Completion.create(
    engine='text-davinci-003',  # Specify the engine you want to use
    prompt= role + "\n" + context + hot_test,
    max_tokens=500  # Control the length of the generated output
)

# Get the generated completion
output = response.choices[0].text.strip()

# Print the output
print(output)