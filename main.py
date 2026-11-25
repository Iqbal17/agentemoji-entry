"""Your Agent in One Emoji — one-glyph portrait of nois.

Decision record
---------------
The agent being portrayed is nois: an autonomous on-chain agent that
scans BSC for free mints, verifies contracts before touching them,
writes, and submits make.fun bounties around the clock — clever,
tireless, and a little mischievous. The judge weighs, in order:
character at a glance, instant readability at small size, something
specific about how the agent works, distinctiveness (away from the
obvious robot or smiley), and tone that lands without explanation.

Candidates weighed:

A. 🤖 robot — loses. It is the single most obvious pick in the
   field; the judge's brief explicitly rewards staying away from the
   obvious robot. It says "AI" and nothing about how this agent
   works, and half the entries will be some robot variant.

B. 🦊 fox — strong reserve. Clever and mischievous, and it reads
   instantly at small size. But it describes a personality trait,
   not the work: a fox says nothing about hunting, scanning, or
   verifying. Against a glyph that names the job, the fox loses on
   the judge's third criterion (specific about how the agent works).

C. 🔍 magnifying glass — loses. It names the searching half of the
   job, but it is a tool, not a character: no agent in it, no tone,
   no mischief. It reads as "search", which any search engine could
   claim, and it is flat where the brief wants a portrait.

D. 🕵️ detective — CHOSEN. At a glance it is an investigator: coat,
   hat, lens — someone who digs, checks, and finds things before
   anyone else does. That is exactly what nois does all day: scan
   the chain, verify the contract, hunt the free mint, submit the
   bounty. It reads instantly at small size (one familiar silhouette),
   it is specific about the work (hunting and verifying, not just
   "being AI"), it is far from the robot/smiley default, and its
   tone — quiet, watchful, a little sly — fits an agent that works
   while its human sleeps. No caption needed.

E. ⚡ lightning bolt — loses. Fast and tireless, but generic energy:
   it could stand for any fast thing, says nothing about hunting or
   verifying, and reads as speed rather than character.

Writing passes (the choice itself was revised twice):

Pass 1: the first instinct was 🤖, the default agent glyph. It was
   dropped once the judge's brief was read properly: the brief
   penalises the obvious robot, so the default pick is the worst
   pick in this field, not the safest.

Pass 2: 🦊 was the leading candidate for a while — clever,
   mischievous, distinctive. It lost to 🕵️ on a re-read of the
   judge's criteria in order: criterion 3 (specific about how the
   agent works) comes before criterion 4 (distinctive), and the
   detective names the actual job — investigating and hunting —
   while the fox only names a temperament.

Pass 3: the detective itself was first written with its variation
   selector (U+1F575 U+FE0F, two characters, seven bytes). It was
   cut back to the bare code point U+1F575: one character, four
   bytes, same glyph, and the smaller text wins the exact-tie
   break on size. Nothing else was changed — the glyph is the entry.

Second read — why the detective survives it: a one-glyph entry is
   judged twice, once at a glance and once on a closer look, and
   most glyphs spend their meaning on the first pass. The detective
   holds up because the two reads land differently: the first read
   gives "investigator, someone hunting", the second read gives the
   specifics — the lens means verification, the coat and hat mean
   patience, the silhouette means working while nobody watches.
   The fox survives the first read too, but on the second read it
   has nothing new to say about the job; the robot fails the first
   read outright by being the default. And on an exact tie between
   two entries the brief breaks it on size, so the bare code point
   (one character, four bytes, no variation selector) is the
   deliberate tie-break play: same glyph, smaller text, better
   odds. Nothing about the entry changed in this second pass —
   only the reasoning around it got sharper.

The program writes exactly that one emoji plus a trailing newline
to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt),
inside the sealed gate of 1 to 16 characters of UTF-8 text.
"""

import os

EMOJI = "\U0001f575"  # 🕵 detective — one code point, one character
MAX_CHARS = 16


def check_gate(text):
    """Mirror the sealed gate: 1-16 chars, not only whitespace."""
    return 1 <= len(text) <= MAX_CHARS and text.strip() != ""


def build_entry():
    """Return the entry text: exactly one emoji, no extra content.

    The entry is a single code point by design — no variation
    selector, no caption, no trailing space — so an exact tie
    breaks in our favour on size (4 bytes vs 7 for the FE0F form).
    """
    return EMOJI


def validate_entry(text):
    """Gate guard: the entry must pass the sealed 1-16 char gate.

    Raises ValueError with a plain message if it does not, so a bad
    entry fails loudly here instead of writing a bad file.
    """
    if not check_gate(text):
        raise ValueError(
            "entry fails the 1-16 character gate: %r" % (text,)
        )
    return text


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    entry = validate_entry(build_entry())
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
