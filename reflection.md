# Reflection on Music Recommender Stress Tests

## High-Energy Pop vs Chill Lofi
High-Energy Pop returned upbeat pop songs with high energy, while Chill Lofi returned slower, moodier lofi tracks. This makes sense because the first profile asked for high energy and pop, and the second asked for a soft, chill lofi vibe.

## High-Energy Pop vs Deep Intense Rock
Both profiles chose high-energy songs, but Deep Intense Rock preferred rock and intense tracks when possible. The system still returned some non-rock high-energy songs because the energy score is very strong, which shows that energy can override genre when the weights are shifted.

## Chill Lofi vs High-Energy Sad
Chill Lofi focused on slow, acoustic-friendly tracks with chill moods. High-Energy Sad still preferred very fast songs because energy was the highest-weighted signal, even though the mood was different. This shows that mixed preferences can be hard for the current scoring logic.

## Why Gym Hero appears for Happy Pop
"Gym Hero" keeps showing up for the Happy Pop profile because it is a pop song with very high energy and low acousticness. Because energy similarity is now weighted more strongly, a song can rank first even if the mood match is not perfect.
