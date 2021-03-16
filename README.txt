This is a machine learning program written in Python that can analyze soil data and determine if it's vulnerable to
erosion or not with over 98.5% accuracy.

Once it has identified the soil, it sends a text message to your phone number via the Twilio API, informing you about the nature of the soil
and giving you advice accordingly.

The ML algorithm that has been implmented for this purpose is Support Vector Machines (SVM), as it is essentially a binary
classification problem with multiple features.

The datasets have been obtained from Kaggle from the AFSIS competition. The features that have been used include 
Sand, Potassium, Calcium, Carbon content and pH value.
