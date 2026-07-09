basic = int(input("Enter Your Basic salary"));
HRA = 0.2*basic;
DA = 0.1*basic;
tot_sal = basic+HRA+DA;
TAX = 0.05*tot_sal;
net = tot_sal - tax; #add some changes
print("Net Salary  is it",net);
