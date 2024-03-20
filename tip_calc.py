# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    tip_calc.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mugwu <mugwu@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/03/13 11:07:48 by mugwu             #+#    #+#              #
#    Updated: 2024/03/13 11:35:35 by mugwu            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

print("Welcome to the tip calculator!")

bill = float(input("What was the bill's total? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many friends are you splitting the bill with? "))

each_person_bill = (bill + (bill * (tip / 100)))/ people
round_bill = round(each_person_bill, 2)
print (f"Each mf finna pay {round_bill}")