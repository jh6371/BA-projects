# python-projects
# 1.Background:
In this project, we have a dataset consist of 40k customer bank account transactions, and it included 

1)TRANSNumber：Customer's transaction number.
2)TimeStamp: The time when customer shopping. 
3)DA:It's the transaction amount of the customer, if it is positive, then it's an income, if it is negative, then it's a consumption.
4)Oper: There are 8 different operations of the account, for example, 1 stands for customer pay for the product from the main account, 2 stands for customer's main account has income, etc. 
5)CTR: It's a customer attribute, including customer's consumption type.

Customer's personality often embeded in their purchase behavior, in my project I try to use their account information and the way they spend money to study their personality. At the same time, if you know one's personality, then you may know what kind of consumption type they may belong to be. This finding may be useful for many part of business market.

# 2. Data 
# 2.1 Data Pre-processing(contributed by my teammates and me):
Before we can dive deep into prediction, we need to deal with the wrong number/ missing value and other issues in our dataset.
1) In this dataset, we have 40 person's transaction record, so we need to shuffle them, and combine them into a single dataset. 2) After this, we found that there are some value is not right, like Oper7 should be negative, while in the dataset it's positive, so we transfered it to negative. 3) We extracted the consumption type of customer from "CTR" and created a new column called classification, also we calculated the 

# 2.2 Variable Creation and dataframe2
In order to predict, we extracted the consumption type of customer from "CTR" and created a new column called classification, also we calculated the the sum of DA in negative and positive, ratio of total values, number of DA in negative and positive,the sum of DA by classification( Superfluous, Investment, Essentials), the number of Oper based on type, count the number of Oper based on type. Then we combine all the varibles we created together as dataframe2.

# 3 Question Defining
In this part, we defined 3 questions to evaluate the customer's personality: Q1.I sometimes run behind my expenses. Q2. I sometimes run behind my expenses. Q3. I often use my saving account to pay the bills.
Options:
A. Very inaccurate 					D. moderately accurate 
B. Moderately Inaccurate 				E.very accurate
C. neither inaccurate nor accurate 

Based on the statistical analysis and common knowledge, we made hypothesis for those 3 questions:
Hypothesis 1: People wIth high ratio of income to expense are more likely to run behind their expenses;
Hypothesis 2: People spend more on superfluous are more likely to make unnecessary purchases;
Hypothesis 3: People spend more frequent by Oper 5 may often pay the bills by saving account.
And we use the boxplot to evaluate which personality they belong to, for example, if a person spend on Oper5 20th percentile of all the people(between 0 to 25) times, he will be regareded as Neuroticism, if he spend on Oper5 about 40th percentile of all people( between 25 and 80) he will be regareded as Agreeableness.

After this, we got every transaction's answer(abcde) for Q1,Q2,Q3, to better use these anwsers for further analysis, we transfered them by using one-hot-encoding.
We also created 5 features: Openness, Conscientiousness, Extraversion, Agreeableness and Neuroticism for further analysis.

# 4 Logistic model:
This part is finished in SAS, we export df2, and using logistic model to get a logistic model, for example: 1.Openness=-2.82276+4.79798*Da_Percentage-0.00002836*Sum_DA_Ess+-0.01518*Num_Oper3-0.01883*Num_Oper4+0.04370*Num_Oper5  
2.Extraversion=-7.30463+0.20116*Num_essencials-0.00012278*Sum_DA_Inv-0.09618*Num_Oper7 
3.Conscientiousness=-6.06908+0.00710*Num_Oper2-0.01951*Oper1
4.Agreeableness=1.08145-0.02073*Num_investment-6.54137*Da_Percentage+0.00001925*Sum_DA_Ess+0.02658*Num_Oper3-0.03348*Num_Oper5
5.Neuroticism=3.45857-0.00823*Num_essencials+0.00000294*Sum_DANeg-2.39417*Da_Percentage

After we get logistic model, we can just replace all the x in this model with encoded answers(one-hot-encoded) in step 3.

And then we can get the number of Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism, this can stand for consumer's personality.

# 5 EDA part: This is fully contributed by my teammates.



 




