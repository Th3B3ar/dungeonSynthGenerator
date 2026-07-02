# Dungeon Synth Generator

A Python script that generates randomized dungeon synth music piece character sheets with subgenre-specific atmospheric, compositional, and texture suggestions.

## Features

**22 Subgenres** - Each with unique thematic content
- Comfy Synth, Cosmic Dungeon Synth, Crypt Hop, Desert Synth, Dino Synth, Dungeon Drone, Dungeon Noise, Dungeon Rap, Egyptian Synth, Fantasy Synth, Food Synth, Forest Synth, J-synth, Keller Synth/Tänzelcore, Nature Synth, Old-school Dungeon Synth, Pirate Synth, Pumpkin Synth, Raw Dungeon Synth, Sea Synth, Winter Synth, and Vampiric Dungeon Synth

**Rich Musical Parameters**
- 15 musical keys (C through Cb)
- 8 musical modes (major, minor, dorian, mixolydian, lydian, phrygian, aeolian, locrian)
- 7 time signatures (4/4, 3/4, 6/8, 5/4, 7/8, 9/8, 12/8)
- 7 tempos (50–160 bpm)
- 30 different musical feels (dark ambient, medieval, forest, castle, haunted, etc.)

**Subgenre-Specific Guidance**
- **Adventure & Setting** - Thematic scene descriptions
- **Ritual / Motif** - Compositional and melodic suggestions
- **Texture / Atmosphere** - Sound design and production tips

**88 Unique Content Items** per category (22 subgenres × 4 items each)

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python's built-in `random` module)

## Installation

### Option 1: Direct Download
1. Download `dungeon_synth_generator.py` from this repository
2. Save it to your desired location
3. Open a terminal/command prompt in that directory

### Option 2: Clone Repository
```bash
git clone https://github.com/yourusername/dungeon-synth-generator.git
cd dungeon-synth-generator
```

## Usage

### Basic Usage
Run the script from your terminal:

```bash
python dungeon_synth_generator.py
```

Each run generates a new randomized character sheet and prints it to your terminal.

### Sample Output
```
============================================================
               DUNGEON SYNTH CHARACTER SHEET                
============================================================

Key:          C
Mode:         minor
Time:         4/4
Tempo:        80 bpm
Subgenre:     Dungeon Drone
Feel:         oppressive crypt

------------------------------------------------------------
                    Adventure & Setting                     
------------------------------------------------------------
- Endless stone corridors of decay
- Deep dungeon resonance and echo
- Oppressive chambers with no escape
- The weight of ages in cold stone

------------------------------------------------------------
                       Ritual / Motif                       
------------------------------------------------------------
- A single sustained note that never wavers
- Slow movement through minor intervals
- Minimal changes creating oppressive consistency
- Deep frequencies that vibrate through stone

------------------------------------------------------------
                    Texture / Atmosphere                    
------------------------------------------------------------
- Sustained, unchanging pad drones
- Deep sub-bass frequencies
- Minimal processing, raw and direct
- No rhythmic elements, purely tonal

============================================================
```

## Subgenres at a Glance

| Subgenre | Best For | Vibe |
|----------|----------|------|
| **Comfy Synth** | Taverns, safe spaces | Warm, inviting |
| **Cosmic Dungeon Synth** | Eldritch horror | Dissonant, alien |
| **Crypt Hop** | Undead, rhythm | Percussive, bouncy |
| **Desert Synth** | Wastelands, oases | Sparse, echoing |
| **Dino Synth** | Prehistoric adventures | Primal, powerful |
| **Dungeon Drone** | Pure atmosphere | Oppressive, tonal |
| **Dungeon Noise** | Chaos, dissonance | Harsh, chaotic |
| **Dungeon Rap** | Verbal combat, bards | Rhythmic, verbal |
| **Egyptian Synth** | Ancient temples | Exotic, ceremonial |
| **Fantasy Synth** | Epic adventure | Heroic, orchestral |
| **Food Synth** | Feasts, celebrations | Playful, cheerful |
| **Forest Synth** | Nature, wilderness | Organic, flowing |
| **J-synth** | Eastern mysticism | Meditative, sparse |
| **Keller Synth / Tänzelcore** | Folk dancing | Rhythmic, danceable |
| **Nature Synth** | Natural harmony | Evolving, organic |
| **Old-school Dungeon Synth** | Retro 80s RPG | Nostalgic, vintage |
| **Pirate Synth** | Seafaring adventure | Swashbuckling, energetic |
| **Pumpkin Synth** | Autumn, Halloween | Whimsical, cozy |
| **Raw Dungeon Synth** | Unfiltered darkness | Harsh, primal |
| **Sea Synth** | Ocean, mystery | Fluid, deep |
| **Winter Synth** | Frozen wastelands | Crystalline, sparse |
| **Vampiric Dungeon Synth** | Gothic elegance | Seductive, dark |

## Customization

### Running Multiple Times
To generate several character sheets in succession:

```bash
for i in {1..5}; do python dungeon_synth_generator.py; done  # macOS/Linux
for ($i=0; $i -lt 5; $i++) { python dungeon_synth_generator.py }  # PowerShell
```

### Modifying the Script
Customize the script by editing:

- **Add a new subgenre**: Add a new entry to `SUBGENRE_CONTENT` with "settings", "motifs", and "textures" lists
- **Add musical parameters**: Extend `KEYS`, `MODES`, `TEMPOS`, `TIME_SIGNATURES`, or `FEELS` lists
- **Adjust output format**: Modify the `print_music_sheet()` function for different formatting

## How to Use the Output

1. **For Composition**: Use the randomized parameters as starting points for your composition
2. **For Inspiration**: Let the randomized combinations spark creative ideas

## File Structure

```
dungeon_synth_generator.py   # Main script
README.md                    # This file
```

## Technical Details

### Code Highlights
- **Consolidated Data Structure**: Single `SUBGENRE_CONTENT` dictionary containing all subgenre data
- **No External Dependencies**: Uses only Python's built-in `random` module
- **Modular Functions**: 
  - `random_music_piece()` - Generates random parameters
  - `print_section()` - Formats output sections
  - `print_music_sheet()` - Orchestrates complete generation and printing
- **Graceful Fallback**: Default content for unknown subgenres

### Performance
- Lightweight: ~18KB file size
- Fast execution: Runs instantly
- Memory efficient: Minimal RAM usage

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request
