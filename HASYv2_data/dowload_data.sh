echo "Downloading dataset"
curl -O https://zenodo.org/record/259444/files/HASYv2.tar.bz2

echo "Unzipping dataset"
bzip2 -d HASYv2.tar.bz2
tar xopf HASYv2.tar

cp symbols.csv ../output_data_alpha_num/
echo "Done"