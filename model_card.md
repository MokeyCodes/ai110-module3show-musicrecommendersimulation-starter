# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeMatcher 1.0**

---

## 2. Goal / Task

This recommender suggests songs from a small catalog based on a user's preferred genre, mood, energy level, and acoustic preference. It tries to predict which tracks will feel like a good match for the user's current listening vibe.

---

## 3. Data Used

The model uses 20 songs from `data/songs.csv`. Each song includes genre, mood, energy, tempo, valence, danceability, and acousticness. The catalog has pop, lofi, rock, ambient, jazz, synthwave, and a few other styles. The dataset is small, so it does not cover all musical tastes or large artist diversity.

---

## 4. Algorithm Summary

The scoring system starts each song at zero and adds points for matching preferences. It gives extra points for genre matches, mood matches, and closeness to the user's target energy. It also adds a small bonus if the song fits the user's acoustic preference. The songs are then ranked by score and the top results are returned.

---

## 5. Observed Behavior / Biases

The system tends to favor songs that match energy because the energy score is strong. Pop and upbeat tracks appear often for energetic profiles. The model can underweight mood when energy is very close, so a song may rank high even if the mood is not an exact match. Because the dataset is small, it can also repeat the same high-energy songs across different profiles.

---

## 6. Limitations and Bias

This recommender is limited by its small catalog and by how the weights are set. Energy similarity is a very strong signal, which can cause a filter bubble around fast, high-energy songs. Users with mixed preferences, like "high energy but moody," may still see mostly upbeat pop hits. The model also does not use lyrics, artist reputation, or user history, so it can miss important taste signals.

---

## 7. Evaluation Process

I tested the system with several user profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and High-Energy Sad. I compared the top 5 results for each profile and checked whether the selected songs matched my intuition. I also changed the scoring weights to make energy more important and watched how the rankings shifted.

---

## 8. Intended Use and Non-Intended Use

This system is designed for classroom exploration and simple music recommendation simulation. It is not intended for real production use or personal music streaming service deployment. It should not be used as a serious playlist engine or to make decisions for a large user audience.

---

## 9. Ideas for Improvement

- Add support for multiple genres and moods in the user profile.
- Use more song features like lyrics mood, artist similarity, or release year.
- Add diversity checks so the top results are not all the same style.

---

## 10. Personal Reflection

My biggest learning moment was seeing how much a single weight change can alter the results. The system still felt like a real recommender even though it is very simple. AI tools helped me structure the code and the evaluation, but I had to double-check the math and the ranking logic myself. I was surprised that energy similarity can dominate so quickly and that the model can feel correct for pure cases but less accurate for mixed preferences. If I extended this project, I would add richer user profiles and more song features so the recommendations are more balanced.
