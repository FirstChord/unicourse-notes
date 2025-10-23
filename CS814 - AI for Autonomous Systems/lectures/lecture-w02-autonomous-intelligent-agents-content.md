---
title: "Week 02 — Autonomous & Intelligent Agents (Lecture Content)"
module: "CS814"
tags: [module/CS814, type/lectures, week-02, content]
date: 2025-10-01
lecturer: "Joseph El Gemayel, Ph.D., FHEA"
---

# Autonomous & Intelligent Agents
*Week 02 Lecture*

***Autonomous & Intelligent Agents***  
Joseph El Gemayel, Ph.D., FHEA  
Teaching Fellow  
Computer & Information Sciences  
Email: joseph.el-gemayel@strath.ac.uk  
Office: LT1214 \- Livingstone TowerPresentation outline  
1\. 2\. 3\. 4\. 5\. 6\. What an agent looks like  
What is meant by “percept” and “percept sequence”  
How to define an agent function and agent program  
How to define properties of agents using PEAS  
How to define properties of environments  
The difference between a reactive (reflex) agent and a  
deliberative (goal/utility-based) agentAutonomous AgentsExample: Roomba  
This Photo by Unknown Author is licensed under CC BY-NC-NDExample: Simplified Roomba versionWhat does an agent look like?What does an agent look like?  
An intelligent agent is an autonomous system that perceives  
its environment through sensors and acts using actuators in a  
way that maximizes the likelihood of achieving its goalsPercept and Percept Sequences  
• A *percept* is a complete set of readings from all of the  
agent’s sensors at a specific timePercept and Percept Sequences  
• A *percept* is a complete set of readings from all of the  
agent’s sensors at a specific time  
• For the robot vacuum cleaner, this will consist of its  
location and whether the floor is clean or dirty  
• Example percept: \[A, dirty\]Percept and Percept Sequences  
• A *percept* is a complete set of readings from all of the  
agent’s sensors at a specific time  
• For the robot vacuum cleaner, this will consist of its  
location and whether the floor is clean or dirty  
• Example percept: \[A, dirty\]  
• A *percept sequence* is a complete ordered list of the  
percept that the agent received since time began  
• Example: \[ \[A, dirty\], \[A, dirty\], \[A, clean\], \[B, dirty\], … \]An Agent Function  
• An *agent function* is a theoretical device which maps  
from any possible percept sequence to an *action*:An Agent Function  
• An *agent function* is a theoretical device which maps  
from any possible percept sequence to an *action*:  
**Percept Action**  
\[A, Clean\] Go to the other room  
\[A, Dirty\] Clean the room  
\[B, Clean\] Go to the other room  
\[B, Dirty\] Clean the room  
… …  
… …An Agent Program  
• An *agent program* is what we run on the architecture  
of the agent to implement the agent function:An Agent Program  
• An *agent program* is what we run on the architecture  
of the agent to implement the agent function:  
function Reflex\_Vacuum\_Agent (\[location, status\]) return an action  
if status \== Dirty then return clean  
else if location \== A then return GoToB  
else if location \== B then return GoToAAn Agent Program  
• An *agent program* is what we run on the architecture  
of the agent to implement the agent function:  
function Reflex\_Vacuum\_Agent (\[location, status\]) return an action  
if status \== Dirty then return clean  
else if location \== A then return GoToB  
else if location \== B then return GoToA  
• What are the clean, *GoToA and GoToB* agent  
functions?Evaluating agent performance  
• How can we evaluate an agent, such as a robotic  
vacuum cleaner?  
• We assess its performance on the task at hand by  
assigning a score  
• The more intelligent the agent, the higher its score  
• Simple agents may score well on simple tasks, but for  
complex tasks, we need more sophisticated agents –  
rational agents that can reason to achieve a high  
scorePEAS  
• To design a rational agent, we must specify the “task  
environment” for the agent  
• We use the acronym PEAS for this:PEAS  
• To design a rational agent, we must specify the “task  
environment” for the agent  
• We use the acronym PEAS for this:  
\- Performance measure: how well does the agent do?  
RVC: amount or % of dirt cleaned up, time taken,  
electricity consumption, noise generated, etc.PEAS  
• To design a rational agent, we must specify the “task  
environment” for the agent  
• We use the acronym PEAS for this:  
\- Performance measure: how well does the agent do?  
\- Environment: what does the agent’s environment  
look like?  
RVC: A, B, dirt, etc.PEAS  
• To design a rational agent, we must specify the “task  
environment” for the agent  
• We use the acronym PEAS for this:  
\- Performance measure: how well does the agent do?  
\- Environment: what does the agent’s environment  
look like?  
\- Actuators: what actuators does the agent have to  
perform its actions with?  
RVC: wheels, different brushes, vacuum extractor,  
etc.PEAS  
• To design a rational agent, we must specify the “task  
environment” for the agent  
• We use the acronym PEAS for this:  
\- Performance measure: how well does the agent do?  
\- Environment: what does the agent’s environment  
look like?  
\- Actuators: what actuators does the agent have to  
perform its actions with?  
\- Sensors: what sensors does the agent have to  
perceive the environment with?  
RVC: dirt detection sensor, location detection  
sensor, etc.PEAS  
• Consider, e.g., the task of designing an Interactive  
tutor (web application):  
\- Performance measure:…  
\- Environment:…  
\- Actuators: …  
\- Sensors: …PEAS  
• Consider, e.g., the task of designing an Interactive  
tutor (web application):  
\- Performance measure:  
\- Improvement in student learning outcomes  
(quiz/test scores, progress over time).  
\- Engagement level (time spent, participation in  
exercises).  
\- Accuracy of feedback and explanations.  
\- Student satisfaction (ratings, continued use)PEAS  
• Consider, e.g., the task of designing an Interactive  
tutor (web application):  
\- Performance measure  
\- Environment:  
\- The student(s) interacting with the web app.  
\- The web platform (browser, device, network  
conditions).  
\- The subject matter content (questions, lessons,  
exercises).PEAS  
• Consider, e.g., the task of designing an Interactive  
tutor (web application):  
\- Performance measure  
\- Environment  
\- Actuators:  
\- On-screen text (explanations, hints,  
corrections).  
\- Interactive elements (quizzes, exercises,  
adaptive content).  
\- Notifications or reminders.PEAS  
• Consider, e.g., the task of designing an Interactive  
tutor (web application):  
\- Performance measure  
\- Environment  
\- Actuators  
\- Sensors:  
\- Student input via keyboard/mouse/touch  
(answers, navigation, typing).  
\- Performance on exercises/quizzes.  
\- Possibly microphone/camera if enabled (voice  
answers, facial expressions).PEAS  
• Consider, e.g., the task of designing an automated  
taxi driver:  
\- Performance:…  
\- Environment:…  
\- Actuators: …  
\- Sensors: …PEAS  
• Consider, e.g., the task of designing an automated  
taxi driver:  
\- Performance: Safe driving, quick trips, passenger  
satisfaction, maximize profits, etc.PEAS  
• Consider, e.g., the task of designing an automated  
taxi driver:  
\- Performance: Safe driving, quick trips, passenger  
satisfaction, maximize profits, etc.  
\- Environment: Roads, other traffic, pedestrians,  
passengers, etc.PEAS  
• Consider, e.g., the task of designing an automated  
taxi driver:  
\- Performance: Safe driving, quick trips, passenger  
satisfaction, maximize profits, etc.  
\- Environment: Roads, other traffic, pedestrians,  
passengers, etc.  
\- Actuators: Steering wheel, accelerator, brake,  
signal, horn, display/speaker, etc.PEAS  
• Consider, e.g., the task of designing an automated  
taxi driver:  
\- Performance: Safe driving, quick trips, passenger  
satisfaction, maximize profits, etc.  
\- Environment: Roads, other traffic, pedestrians,  
passengers, etc.  
\- Actuators: Steering wheel, accelerator, brake,  
signal, horn, display/speaker, etc.  
\- Sensors: Cameras, sonar, speedometer, GPS,  
odometer, engine sensors, keyboard, etc.Properties of environments  
• An unknown and cluttered room with other agents in it  
is a more difficult place to live in than an empty room  
• A simple task in a simple environment means that we  
can get top performance out of a simple agent  
• A complex task in a complex environment requires a  
very sophisticated agent  
• Consider the task and environment for an automated  
taxi driver\!Dimensions of the environment  
• We use six dimensions to define the environment:  
\- Fully observable (or partially observable)?  
An agent's sensors give it access to the complete  
state of the environment at each point in timeDimensions of the environment  
• We use six dimensions to define the environment:  
\- Fully observable (or partially observable)?  
\- Single agent (or multi-agent)?  
An agent operating by itself in an environmentDimensions of the environment  
• We use six dimensions to define the environment:  
\- Fully observable (or partially observable)?  
\- Single agent (or multi-agent)?  
\- Deterministic (or stochastic or strategic)?  
The next state of the environment is completely  
determined by the current state and the action  
executed by the agentDimensions of the environment  
• We use six dimensions to define the environment:  
\- Fully observable (or partially observable)?  
\- Single agent (or multi-agent)?  
\- Deterministic (or stochastic or strategic)?  
\- Episodic (or sequential)?  
The agent's experience is divided into atomic  
"episodes“Dimensions of the environment  
• We use six dimensions to define the environment:  
\- Fully observable (or partially observable)?  
\- Single agent (or multi-agent)?  
\- Deterministic (or stochastic or strategic)?  
\- Episodic (or sequential)?  
\- Static (or dynamic or semi-dynamic)?  
Environment is unchanged while an agent is  
deliberatingDimensions of the environment  
• We use six dimensions to define the environment:  
\- Fully observable (or partially observable)?  
\- Single agent (or multi-agent)?  
\- Deterministic (or stochastic or strategic)?  
\- Episodic (or sequential)?  
\- Static (or dynamic or semi-dynamic)?  
\- Discrete (or continuous)?  
A limited number of distinct, clearly defined  
percepts and actionsDimensions of the environmentDimensions of the environmentDimensions of the environmentDimensions of the environmentDimensions of the environmentReactive Agents  
• If an agent only “reacts” to its current percept, we call  
it a reactive (or reflex) agent  
• Actions are chosen rules of the form “if condition then  
action” (or something equivalent to this)  
• Examples: the simple vacuum cleaner controller  
• Good performance only at simple tasks – would need  
an unfeasibly large number of rules for a complicated  
task, such as playing chessDeliberative AgentsDeliberative Agents  
• Deliberation is the process of thinking about how your  
actions will affect the world before committing to it  
• Given a choice of actions, choose the one that gets  
you closer to your goals, or closer to a state of high  
utility  
• Since the goal or state of high utility may be some  
way off, need to think about sequences of actions  
• This leads to a *search problem…*Room & Heating Thermostats  
• **Performance Measure**: …  
• **Environment**: …  
• **Actuators**: …  
• **Sensors**: …Room & Heating Thermostats  
• **Performance Measure**: Maintaining user-set  
temperature (Primary), Low Energy Consumption  
(Secondary)  
• **Environment**: House / Room(s)  
• **Actuators**: Start the Heating /  
Stop the Heating /  
No Operation  
• **Sensors**: One or more  
temperature sensors installed  
in different rooms / placesRoom & Heating Thermostats  
• **Fully Observable?**  
• **Deterministic?**  
• **Episodic?**  
• **Static?**  
• **Discrete?**  
• **Single agent?**Room & Heating Thermostats  
• **Fully Observable?** Yes  
• **Deterministic?** Yes, if …  
• **Episodic?** No  
• **Static?** No  
• **Discrete?** Yes  
• **Single agent?** Yes  
