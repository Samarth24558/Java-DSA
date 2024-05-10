read -p "Enter the limit: " limit
i=1
while [ $i -le $limit ];
do
	echo $i
	i=$((i+1))
done

