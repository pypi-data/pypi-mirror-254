def print_prog():
    print(
        """
import gender_guesser.detector as gender
def gender_classifier(name):
    d = gender.Detector()
    gender_prediction=d.get_gender(name)
    return gender_prediction
name_to_classify="Jennifer"
predicted_gender=gender_classifier(name_to_classify)
if predicted_gender in ['male','female']:
    print(f"the predicted gender for{name_to_classify} is {predicted_gender}:")
else:
        print(f"the predicted gender is invalid for{name_to_classify}:")

"""
    )
