#starting term of Arithmetic Progressions
ap1_a=3 
ap2_a=5 
ap3_a=15
#common difference
ap1_cd=3 
ap2_cd=5 
ap3_cd=15
#ending term
ap1_l=999
ap2_l=995
ap3_l=990
#their respective sums
ap1_sum=(ap1_a+ap1_l)/2*(((ap1_l-ap1_a)//3)+1)
ap2_sum=(ap2_a+ap2_l)/2*(((ap2_l-ap2_a)//5)+1)
ap3_sum=(ap3_a+ap3_l)/2*(((ap3_l-ap3_a)//15)+1)
print(int(ap1_sum+ap2_sum-ap3_sum))