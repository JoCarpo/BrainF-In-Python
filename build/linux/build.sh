dir=$(pwd)

cp brainf.sh ~/
cd ../../
cp -r src ~/
cd ~/
mv src .brainf
mv brainf.sh .brainf.sh
echo "source ~/.brainf.sh" >> .bashrc

echo Type 'brain' followed by your file name, to run BrainF***

cd dir
