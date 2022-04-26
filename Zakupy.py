shopping_dict={
    "piekarnia": ['chleb'.capitalize(), 'pączek'.capitalize(), 'bułki'.capitalize()],
    "warzywniak": ['marchew'.capitalize(), 'seler'.capitalize(), 'rukola'.capitalize()]
}

for i in shopping_dict:
    print("Idę do "+i.capitalize()+", kupuję tu następujące rzeczy" +str(shopping_dict[i]))

