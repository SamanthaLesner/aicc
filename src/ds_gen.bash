set -o errexit
set -o nounset
set -o pipefail

# set -o xtrace
# set -o verbose
# set -o errtrace

parallel="-P 12"
# parallel=""

vgen()
{
    img=$1
    convert ${img} -flop  ${img}_flop.png
    convert ${img} -resize '80%' ${img}_resized_80.png
    convert ${img} -resize '90%' ${img}_resized_90.png
    convert ${img} -rotate 5 ${img}_rotated_p5.png
    convert ${img} -rotate -5 ${img}_rotated_n5.png
}; export -f vgen

rm -f data/*cview* ; 

find data -type f \
    | { egrep -v cview || true ; } \
    | xargs -i $parallel bash -c \
    "
        python src/image_split4j.py {} < {}
    "

find data -type f -name '*cview*' \
    | xargs -i $parallel bash -c \
    '
        p={}; 
        deps/realesrgan-ncnn-vulkan-20220424-windows/realesrgan-ncnn-vulkan.exe -i ${p} -o ${p}_upscaled.png
    '

find data -type f -name '*cview*' \
    | xargs -i $parallel bash -c \
    "
        vgen {}
    "