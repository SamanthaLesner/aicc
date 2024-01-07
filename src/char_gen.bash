

char_data_cat()
{
    cat <<EOF
Benny Badger - A friendly and adventurous badger. 
Sally Squirrel - A quick and witty squirrel with lots of energy.
Percy Porcupine - A shy but clever porcupine.
Freddie Frog - A jovial and jumping frog who loves the water.
Ollie Otter - A playful and clever otter who's always up for a game.
Daisy Duck - A cheerful and chatty duck who loves to swim.
Ginger Gopher - A hardworking and helpful gopher.
Wally Woodpecker - A peppy and persistent woodpecker with a love for music.
Rita Rabbit - A quick and kind rabbit with a big family.
Harvey Hedgehog - A curious and careful hedgehog who loves to explore.
Tilly Turtle - A wise and patient turtle who takes life slowly. 
Felix Fox - A clever and cunning fox with a heart of gold.
EOF
} ; export -f char_data_cat


char_data_cat \
    | cut -d" " -f1,2 \
    | perl -pe\
'
chomp;
s{ }{_}g;
s{ *$}{.png\n}g;
' | sort


char_data_cat \
    | cut -d" " -f4- 