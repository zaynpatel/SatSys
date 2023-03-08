### Notes from a fireside chat with [Alex Epshteyn](https://www.linkedin.com/in/alex-epshteyn-9201832/)
Background: Each week in Satellite Systems, an ECE and MechE elective, at Olin College of Engineering, our professor Dr. Whitney Lohmeyer brings in a speaker. This week our class heard from Alex, Team Lead of Regulatory Affairs and Spectrum Engineering at Amazon Kupier, a division of Amazon focused on launching Low Earth Orbit (LEO) satellites to provide broadband internet connection to customers. 

_Most of my notes are concepts Alex mentioned during the chat that I was unaware of. So, below you'll find paragraphs of research instead of bulleted insights._

**Question:** What is ITU?

**Answer:** It's an agency that focuses on expanding internet communication technology (ICT) to the world, especially places that don't have access to broadband internet. They operate via membership of states (who are opting into participating in the spread of digital technology) and companies (who are building satellite infrastructure to make the goal real). The ITU was created in partnership with the French Government and 20 European States who decided in 1865 that there needed to be a framework for telegraphy equipment (any device that permits information sharing via a signal over a distance), common operating standards, and economics (answer the question: how would international policy and financial instruments, like tarrifs, work).

Countries not apart of the ITU don't get the benefits of global telecommunication standards, coordination of radio-frequency spectrum, support for the deployment and development of satellite technologies. 

_How does not being apart of the ITU make life harder?_ The current answer is: countries who aren't apart don't get benefits. But I'd be curious about how much of an impact these benefits make.

_If a country isn't part of the ITU, does this mean companies that operate in non-ITU countries don't get benefits._ The current answer is: Companies don't need to be a member to get the benefits or operate in other non-ITU countries. 

_Question(s) I'd like to answer: a) How successful is the UN in governing telecommunications infrastructure (ex: ITU) or allocating capital and resources for their goals (UN SDGs). The UN has percieved influence and has become a default resource for people curious about solving big problems in the social + technology sector but I wonder how helpful it really is. b) Governance in early stages, like the ITU starting seems to have good intent and high follow through. I wonder how the early stages of government are run similar to a startup and if there are built-in parts of governance that force organizations like ITU into a different operating model (that's better/worse than a startup, I don't know). I think answering (b) brings me closer to understanding where the strengths of government are and how true the scrutinizations are._

**Question:** What is C/N and I/N and why are they important for satellite systems?

**Answer:** C/N is carrier (C refers to carrier wave of a modulated signal, modulated meaning: a modification to a signal as it's transmitted from sender to reciever) to noise ratio and is the ratio of the signals power, which is measured at the input stage, to the signals noise, also measured at the input stage. Noise is either thermal or external. Thermal is inherent to the electrical system! For example, the movement of electrons in the circuit could cause noise. External noise can be interference from other electrical systems, radios, satellites, anything that's picked up from the reciever. Tactics like physical shielding and wiring can be used to prevent or reduce external noise from interfering with a satellite system. 

I/N is interference to noise ratio and is the ratio of interfering signals to the noise of a communication system. It represents the level of interference that's present in a communication system. 

C/N measures **strength and quality of signal** while I/N measures **level of interference.** 

**Question:** What is a link budget?

**Answer:** A link budget, similar to a corporate financial budget, accounts for something. In this case, it's accounting all power gains (when a signal is amplified) and losses (when signal is weakened through cable) that a communication signal experiences during transmission (ex: from a ground station to a satellite). The link budget can be calculated in real time as the output calculation helps in discerning if the signal to noise ratio (calculated by recieved signal power (calculated by adding transmitter power, antenna and amplifier gains **and** subtracting losses)/noise power (sum of atmospheric, receiver, thermal) is adequate.

In the link budget calculation, the numbers calculated include: path loss (loss of energy as it moves from transmitter to reciever), gain (adding energy via a power supply), strength of signal, power of a signal.

**Question:** What is adaptive coding modulation (ACM)?

**Answer:** ACM is a technique used to adapt the coding scheme to transmit data based on the communication link. For example, if a customer has a lower bandwith reception, ACM allows the transmitter to shift the strength of signal, interference, and noise to complete the data transfer. _Research the schemes it uses: Binary Phase-Shift Keying (BPSK), Quadrature Phase-Shift Keying (QPSK), Reed-Solomon codes, Low-Density-Parity-Check. I wonder when and where ACM is used specifically and how a system designer builds it for multiple scenarios._

**Question:** What is unavailability in satellite communications?

**Answer:** Unavailability is a period of time when the reciever and transmitter can't send signal. It's typically due to atmospheric conditions (rain, fog, snow can interrupt the communication link), equipment failure, interference. 

_Rain fade (degredates signal and increases losses) is a frequent problem in satellite communications. I'd be curious about other weather related problems in satellites and adjacent industries where dedicated teams work on weather resistant systems. EV performance based on weather might be an interesting adjacent topic to research. Fundamentally, these are all EE problems._
