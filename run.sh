rm wiki -r 2> /dev/null
scp -r ryo@home.wakatabe.com:/usr/local/www/docs/home.wakatabe.com/ryo/wiki/wiki . 

cp getEdges.py wiki
cd wiki
outfile=a
rm ../$outfile 2> /dev/null
echo "digraph wiki {" >> ../$outfile
echo "graph [ layout = fdp ];" >> ../$outfile

for i in $(ls *.txt); do
    python getEdges.py $i >> ../$outfile
done
echo "}" >> ../$outfile
cd -
