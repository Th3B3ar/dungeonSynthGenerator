import random

# ---------------------------------------------------------------------------
# Content pools for dungeon-synth music piece generation
# ---------------------------------------------------------------------------

KEYS = ["C", "G", "D", "A", "E", "B", "F#", "C#", "F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb"]
TIME_SIGNATURES = ["4/4", "3/4", "6/8", "5/4", "7/8", "9/8", "12/8"]
FEELS = [
    "dark ambient", "medieval", "forest", "castle", "ruins",
    "ritual", "mystical", "haunted", "ice wind", "ancient crypt",
    "arcane", "tavern", "moonlit", "wandering", "necromancy",
    "stone hall", "cavern", "sorcery", "grimwood", "eldritch",
    "frosted keep", "forgotten shrine", "spectral", "dusk march",
    "labyrinth", "wyrm lair", "monolith", "eldersong", "blood moon",
    "verdant glade"
]
MODES = ["major", "minor", "dorian", "mixolydian", "lydian", "phrygian", "aeolian", "locrian"]
TEMPOS = ["50 bpm", "65 bpm", "80 bpm", "100 bpm", "120 bpm", "140 bpm", "160 bpm"]

# Consolidated subgenre content: settings, motifs, and textures
SUBGENRE_CONTENT = {
    "Comfy Synth": {"settings": ["- A warm hearth in a cozy tavern", "- Soft candlelight in a peaceful inn", "- A comfortable chamber by the fireplace", "- Gentle melodies from a quiet corner"], "motifs": ["- Warm, repeating chord progressions that embrace the listener", "- Soft arpeggios that evoke hearth and home", "- Gentle melodic phrases that comfort and console", "- Layered pads creating a warm, enveloping atmosphere"], "textures": ["- Warm analog synth pads with slight saturation", "- Soft strings and pads layered together", "- Lo-fi samples with tape warmth", "- Gentle reverb and delay creating intimacy"]},
    "Cosmic Dungeon Synth": {"settings": ["- Ancient star charts and cosmic runes", "- Beneath alien moons in forgotten realms", "- Eldritch dimensions beyond mortal comprehension", "- Celestial horrors watching from the void"], "motifs": ["- Dissonant intervals suggesting alien dimensions", "- Droning bass notes anchoring cosmic horror", "- Ethereal melodies that seem from beyond space", "- Sharp, piercing synth lines cutting through the void"], "textures": ["- Detuned, dissonant pad layers", "- Digital artifacts and glitches suggesting malfunction", "- Reverb-drenched tones suggesting infinite space", "- Metallic textures and crystalline harmonics"]},
    "Crypt Hop": {"settings": ["- Bone-laden crypts and sealed tombs", "- Echoes of ancient undead guardians", "- Pillaged burial chambers with cursed treasures", "- Skeletal dancers in the shadows"], "motifs": ["- Skeletal rhythm patterns with bouncing basslines", "- Staccato melodies mimicking skeletal movements", "- Percussion-driven motifs with undead swagger", "- Syncopated patterns that march with purpose"], "textures": ["- Crisp, punchy drum machines and percussion", "- Dry, direct synth tones without warmth", "- Rhythmic loops with industrial edge", "- Sharp attack on all percussion and synth hits"]},
    "Desert Synth": {"settings": ["- Endless dunes under burning suns", "- Hidden oases with forbidden secrets", "- Crumbling temples in the wasteland", "- Mirages and sandstorms in barren lands"], "motifs": ["- Sparse, isolated notes suggesting vast emptiness", "- Pentatonic scales evoking Middle Eastern sounds", "- Reverb-heavy tones suggesting desert echoes", "- Gradually shifting arpeggios like shifting sands"], "textures": ["- Breathy, wind-like textures and tones", "- Vast reverb suggesting endless space", "- Dry, dusty string and pad samples", "- Sparse arrangement with lots of empty space"]},
    "Dino Synth": {"settings": ["- Prehistoric jungles with towering giants", "- Lost valleys where dinosaurs still roam", "- Fossilized temples of ancient civilizations", "- Survival in a primordial world"], "motifs": ["- Low, rumbling bass patterns like distant footsteps", "- Primal, simple melodies suggesting primitive life", "- Percussive synth hits mimicking roars and calls", "- Adventurous rising melodies like exploration"], "textures": ["- Deep, resonant bass frequencies", "- Growling, primal synth sounds", "- Nature field recordings mixed with synths", "- Heavy compression creating power and presence"]},
    "Dungeon Drone": {"settings": ["- Endless stone corridors of decay", "- Deep dungeon resonance and echo", "- Oppressive chambers with no escape", "- The weight of ages in cold stone"], "motifs": ["- A single sustained note that never wavers", "- Slow movement through minor intervals", "- Minimal changes creating oppressive consistency", "- Deep frequencies that vibrate through stone"], "textures": ["- Sustained, unchanging pad drones", "- Deep sub-bass frequencies", "- Minimal processing, raw and direct", "- No rhythmic elements, purely tonal"]},
    "Dungeon Noise": {"settings": ["- Chaos and dissonance in the deep dark", "- Mechanical sounds of ancient traps", "- Screeching from unseen horrors", "- Discordant echoes through twisted halls"], "motifs": ["- Chaotic layers of clashing frequencies", "- Abrupt, dissonant chord changes", "- Atonal melodies with no clear resolution", "- Random pitch shifts and texture variations"], "textures": ["- Distorted, overdriven synth signals", "- Layered noise and white noise bursts", "- Harsh filtering and modulation", "- Chaotic mixing and unpredictable textures"]},
    "Dungeon Rap": {"settings": ["- Verbal spellcasting and magical rhymes", "- Tavern bards with cunning wordplay", "- Battle chants echoing through stone halls", "- Legends told to a steady beat"], "motifs": ["- Rhythmic, repetitive basslines driving the narrative", "- Vocal-like synth melodies that speak and sing", "- Call-and-response patterns between synth voices", "- Percussive hits on strong beats for emphasis"], "textures": ["- Punchy, defined beats and samples", "- Vocal-like synth textures and processing", "- Tight compression and EQ", "- Clear, articulate percussion and bass"]},
    "Egyptian Synth": {"settings": ["- Pyramids under the Nile's watchful gaze", "- Pharaonic rituals and golden treasures", "- Temple hieroglyphics glowing with power", "- Desert kingdoms of sand and stone"], "motifs": ["- Exotic scales and modal progressions", "- Repetitive patterns suggesting ceremonial rituals", "- Ornate, decorative melodic flourishes", "- Deep, resonant drones like temple bells"], "textures": ["- Exotic string arrangements and sitar samples", "- Warm, resonant tones suggesting ancient instruments", "- Ornate pad layers with modal richness", "- Reverb suggesting temple acoustics"]},
    "Fantasy Synth": {"settings": ["- Mystical forests with ancient magic", "- Castles of splendor and tragedy", "- Enchanted realms beyond the veil", "- Quest for glory in fantastical lands"], "motifs": ["- Soaring, heroic melodies that inspire adventure", "- Major key progressions suggesting triumph", "- Layered instruments creating richness and depth", "- Sweeping arpeggios like magical incantations"], "textures": ["- Lush, orchestral pad arrangements", "- Layered strings, woodwinds, and brass tones", "- Rich harmonic content and depth", "- Swelling dynamics and expressive modulation"]},
    "Food Synth": {"settings": ["- Kitchens bubbling with alchemical broths", "- Feasts celebrating heroic deeds", "- Spice markets and culinary adventures", "- A banquet in the great hall"], "motifs": ["- Bubbly, effervescent synth lines", "- Bouncy, energetic melodies full of character", "- Playful interactions between different voices", "- Warm, satisfying harmonic progressions"], "textures": ["- Bright, cheerful synth tones", "- Bubbly, playful textures and effects", "- Warm, satisfying harmonic character", "- Clean, energetic presentation"]},
    "Forest Synth": {"settings": ["- Whispering trees and ancient groves", "- Sunlight filtering through dense canopy", "- Woodland creatures watching from shadows", "- Paths winding through primordial wilderness"], "motifs": ["- Organic, flowing melodic lines", "- Natural-sounding scales and intervals", "- Layered textures suggesting rustling leaves", "- Gentle, wandering patterns like forest paths"], "textures": ["- Organic, natural-sounding instruments", "- Ambient field recordings of nature", "- Soft, flowing pad textures", "- Acoustic instruments blended with synths"]},
    "J-synth": {"settings": ["- Bamboo groves and mountain temples", "- Samurai honor in moonlit nights", "- Cherry blossoms falling on ancient stones", "- Eastern mysticism and martial traditions"], "motifs": ["- Pentatonic melodies with Eastern sensibility", "- Restrained, meditative phrasing", "- Subtle bends and microtonal adjustments", "- Sparse notes with meaningful silence between them"], "textures": ["- Clean, pristine digital synth tones", "- Sparse, minimal arrangement philosophy", "- Subtle, refined processing", "- Balanced, meditative mixing"]},
    "Keller Synth / Tänzelcore": {"settings": ["- Medieval village dances and celebrations", "- Folk traditions preserved in time", "- Rhythmic stomping in the square", "- Community rituals and gatherings"], "motifs": ["- Repetitive, danceable rhythmic patterns", "- Folk-inspired melodic turns and flourishes", "- Strong, clear beat emphasis", "- Circular progressions that encourage movement"], "textures": ["- Acoustic and acoustic-modeled instruments", "- Clear, punchy percussion and drums", "- Warm, earthiness in the tonal character", "- Natural resonance and ambience"]},
    "Nature Synth": {"settings": ["- Wild untamed landscapes", "- Harmony with the natural world", "- Seasons turning in perpetual cycles", "- Life and growth in verdant abundance"], "motifs": ["- Cycling patterns mimicking natural rhythms", "- Harmonies based on overtone series", "- Gradually evolving, never static", "- Balanced major and minor qualities"], "textures": ["- Sampled natural sounds and creatures", "- Organic, evolving pad textures", "- Warm and inviting sonic character", "- Ecological balance in the mix"]},
    "Old-school Dungeon Synth": {"settings": ["- Classic dungeon crawling adventures", "- Retro RPG campaigns come alive", "- 80s-inspired fantasy realms", "- Nostalgia for forgotten eras"], "motifs": ["- Classic 80s synthesizer patches and progressions", "- Vintage chord sequences from RPG soundtracks", "- Simple but effective melodic hooks", "- Retro reverb and delay effects on every note"], "textures": ["- Vintage synthesizer patches and tones", "- Analog warmth and slight harmonic saturation", "- Classic reverb and delay effects", "- Retro production values and aesthetics"]},
    "Pirate Synth": {"settings": ["- Sailing the high seas for treasure", "- Coastal taverns filled with rogues", "- Sunken ships and buried gold", "- Freedom on the boundless ocean"], "motifs": ["- Swaying, rhythmic patterns like ocean waves", "- Adventurous, roguish melodic leaps", "- Shanty-like chord progressions and rhythms", "- Energetic variations that build excitement"], "textures": ["- Swashbuckling, adventurous synth character", "- Warm, nautical tones and textures", "- Dynamic, energetic production style", "- Action-oriented, driving presentation"]},
    "Pumpkin Synth": {"settings": ["- Autumn festivals and harvest moons", "- Carved jack-o'-lanterns glowing in darkness", "- Haunted cornfields and spiced ciders", "- Cozy nights before All Hallows' Eve"], "motifs": ["- Whimsical, slightly spooky melodic turns", "- Seasonal chord progressions in minor and major", "- Playful dissonance mixed with consonance", "- Nostalgic melodies with autumnal warmth"], "textures": ["- Autumn-toned, warm color palette", "- Playful, whimsical synth sounds", "- Nostalgic, vintage production qualities", "- Slightly spooky reverb and ambience"]},
    "Raw Dungeon Synth": {"settings": ["- Unfiltered darkness and raw power", "- Stripped-down dungeons of pure dread", "- Unpolished evil lurking in the depths", "- Primal and visceral underground realms"], "motifs": ["- Distorted, unrefined synth tones", "- Harsh intervals creating discomfort", "- Simple, primal rhythmic patterns", "- Aggressive, unpolished melodic lines"], "textures": ["- Harsh, unpolished synth tones", "- Minimal mixing and processing", "- Aggressive, confrontational sound", "- Direct, unrefined sonic presentation"]},
    "Sea Synth": {"settings": ["- Shipwrecks on foggy shores", "- Merfolk mysteries in the deep", "- Storm-tossed waves and salt spray", "- Lighthouse beams cutting through mist"], "motifs": ["- Undulating patterns like waves and tides", "- Haunting, mysterious melodic fragments", "- Long, sustained tones suggesting vast depths", "- Fluid, flowing transitions between phrases"], "textures": ["- Fluid, watery synth effects", "- Deep, resonant subsonic frequencies", "- Undulating, wave-like modulation", "- Mysterious, misty reverb and ambience"]},
    "Winter Synth": {"settings": ["- Frozen wastelands of eternal snow", "- Icy castles piercing clouded skies", "- Blizzards raging across white tundras", "- Survival in bitter cold and darkness"], "motifs": ["- High, crystalline synth tones like ice", "- Sparse, isolated notes suggesting desolation", "- Slow, freezing progression of chords", "- Piercing, sharp melodic lines cutting through cold"], "textures": ["- Crystalline, high-frequency synth tones", "- Cold, clear digital character", "- Sparse, isolated sonic elements", "- Icy reverb suggesting frozen landscapes"]},
    "Vampiric Dungeon Synth": {"settings": ["- Gothic castles and undead nobility", "- Crimson halls where blood flows eternal", "- Midnight hunts through shadowed streets", "- Immortal darkness and seductive dread"], "motifs": ["- Seductive, hypnotic rhythmic patterns", "- Sensual, minor-key melodies", "- Elegant, aristocratic chord progressions", "- Predatory, flowing movement through phrases"], "textures": ["- Seductive, smooth pad layers", "- Dark, sensual harmonic coloration", "- Elegant, refined production", "- Mysterious, enigmatic atmosphere"]},
}

SUBGENRES = list(SUBGENRE_CONTENT.keys())

DEFAULT_CONTENT = {
    "settings": ["- Candlelit halls and forgotten ruins", "- Frosted towers and moonlit rites", "- Arcane rituals and spectral echoes", "- Wandering through ancient groves"],
    "motifs": ["- Use modal step motion, simple chant lines,", "- or repeated arpeggios to evoke old-world mood.", "- Consider the feel and mode when shaping melody", "- Let the subgenre guide your compositional choices"],
    "textures": ["- Layer pads, choir-like drones, lo-fi keys,", "- or distant percussion to create a ritual feel.", "- Consider ambient qualities and spatial effects", "- Let reverb and delay shape the atmosphere"]
}


def random_music_piece():
    """Generate a random music piece descriptor."""
    return {
        "key": random.choice(KEYS),
        "time_signature": random.choice(TIME_SIGNATURES),
        "feel": random.choice(FEELS),
        "subgenre": random.choice(SUBGENRES),
        "tempo": random.choice(TEMPOS),
        "mode": random.choice(MODES),
    }


def print_section(title, items):
    """Print a formatted section with title and bulleted items."""
    print("\n" + "-" * 60)
    print(title.center(60))
    print("-" * 60)
    for item in items:
        print(item)


def print_music_sheet(piece):
    """Print a randomly generated dungeon-synth music piece to the terminal."""
    content = SUBGENRE_CONTENT.get(piece["subgenre"], DEFAULT_CONTENT)
    
    print("\n" + "=" * 60)
    print("DUNGEON SYNTH CHARACTER SHEET".center(60))
    print("=" * 60 + "\n")
    
    print(f"Key:          {piece['key']}")
    print(f"Mode:         {piece['mode']}")
    print(f"Time:         {piece['time_signature']}")
    print(f"Tempo:        {piece['tempo']}")
    print(f"Subgenre:     {piece['subgenre']}")
    print(f"Feel:         {piece['feel']}")
    
    print_section("Adventure & Setting", content["settings"])
    print_section("Ritual / Motif", content["motifs"])
    print_section("Texture / Atmosphere", content["textures"])
    
    print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    piece = random_music_piece()
    print_music_sheet(piece)
