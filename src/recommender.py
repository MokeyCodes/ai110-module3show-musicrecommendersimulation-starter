from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: "pop"
    favorite_mood: "intense"
    target_energy: 0.9
    likes_acoustic: True

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs: List[Dict] = []
    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": int(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }
            songs.append(song)
    return songs

def score_song(song: Dict, user_prefs: Dict) -> Tuple[float, List[str]]:
    """Judge a single song against the user's preferences."""
    score = 0.0
    reasons: List[str] = []

    if song.get("genre") == user_prefs.get("genre"):
        score += 2.0
        reasons.append("genre match (+2.0)")

    if song.get("mood") == user_prefs.get("mood"):
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_similarity = 1.0 - abs(song.get("energy", 0.0) - user_prefs.get("energy", 0.0))
    energy_score = 2.0 * energy_similarity
    score += energy_score
    reasons.append(f"energy match (+{energy_score:.2f})")

    likes_acoustic = user_prefs.get("likes_acoustic")
    if likes_acoustic is True and song.get("acousticness", 0.0) >= 0.5:
        score += 0.5
        reasons.append("acoustic match (+0.5)")
    elif likes_acoustic is False and song.get("acousticness", 1.0) <= 0.3:
        score += 0.5
        reasons.append("low acousticness match (+0.5)")

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, List[str]]]:
    """Return the top-k scored songs for a user preference profile."""
    scored_songs = [
        (song, *score_song(song, user_prefs))
        for song in songs
    ]

    ranked_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    return ranked_songs[:k]
