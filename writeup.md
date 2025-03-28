## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

There's a chance that if you had a data set with a lot of missing or "NO DATA" values, filtering it out could lead to a misinterpretation of the data set and could result in outliers or an irregurlar pattern that could jump from high to low or vice versa.

## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

It seems like sleep occurs for phase 0 where the maximum heartrate is below 100 BPM and average is under 65 BPM. The graphs also show that more values for theose phases were closer to the lower end of values. This phase also has the lowest standard deviation suggesting that the heart rate was relatively consistent during this phase when compared to the others which is what you'd expect during sleep. 

## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings. 

Phase 2 has the highest maximum heart rate and more spikes in heart rate, shown throw the graph and its high standard deviation suggesting that heart rate is changing rapidly like it would when someone is excerising. 

## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

Phase 3 has a has a lower average heart rate as well as a realively high standard deviation suggestion that theres wide variation in heart during that phase.
