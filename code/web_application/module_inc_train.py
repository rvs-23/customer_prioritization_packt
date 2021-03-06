import datetime
from sklearn.preprocessing import StandardScaler
import joblib

def inc_train(data_stream, prediction_date):
    """
    Function to inc. train the ml model on data from prediction_date - 3 days
    :param data_stream: the object that lets us retrieve the input data, data type: module_dep.Datastream object
    :param prediction_date: the date for which the prediction report was generated, data type: datetime.date object
    :return: None
    """
    
    # getting the date from three days ago to train the model
    three_days_ago = prediction_date - datetime.timedelta(days=3)
    df_inc_train = data_stream.get_data(three_days_ago)
    
    # Seperating the features and labels 
    X = df_inc_train.drop(columns=['email', 'date', 'conversion_status'])
    y = df_inc_train['conversion_status']
    
    # Fixing the feature set chosen
    feature_set_1 = ['transactions_amount', 'count_pay_attempt', 'nunique_beacon_type',
                     'count_user_stay', 'count_buy_click', 'profile_submit_count',
                     'sum_beacon_value']
    # feature_set_5 = ['count_pay_attempt', 'count_buy_click',
    #                  'nunique_report_type', 'profile_submit_count']
    
    # Scaling the X
    X_scaled = StandardScaler().fit_transform(X[feature_set_1])
    
    model_chosen = 'SDC_f1_s_jlib.pkl'
    model = joblib.load(model_chosen)
    # Partial fitting to the model data from 3 days ago and updating model_chosen
    model.partial_fit(X_scaled, y)
    joblib.dump(model, model_chosen)
    return None

#################################################################################
