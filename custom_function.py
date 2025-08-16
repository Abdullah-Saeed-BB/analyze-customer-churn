def feature_names_out(self, input_features): return input_features

# Map for LOYAL customers
loyal_customer_map = {
    # --- High-Value Indicators ---
    'TotalCharges': '**High-Value Customer Alert:** This customer has a major spending history. Acknowledge them with a personal thank you, assign a dedicated account manager, or offer exclusive perks.',
    'tenure': 'A long-term, loyal customer. Invite them to an exclusive "insider" program or offer them a loyalty appreciation bonus, like a free month of service.',
    'MonthlyCharges': 'This customer is happy with their plan\'s value. Reinforce this by offering to lock in their current rate, or introduce them to low-cost, high-impact add-ons.',

    # --- Strong Commitment Indicators ---
    'Contract_Two year': 'This is your most secure customer type. Send a "thank you" gift near their renewal date to encourage another long-term commitment.',
    'PaymentMethod_Credit card (automatic)': 'This customer values convenience. Ensure their billing is seamless and perhaps offer them other "set-and-forget" services like automatic device protection.',

    # --- Upsell Opportunity Indicators ---
    'InternetService_DSL': 'This loyal customer might be ready for an upgrade. Offer them a special "loyalty discount" to move to a faster Fiber Optic plan.',
    'StreamingMovies_Yes': 'This customer is an engaged media user. They are a prime candidate for premium channel packages or a speed upgrade for better 4K streaming quality.',
    'StreamingTV_Yes': 'This customer actively uses our TV service. Promote related add-ons like extra sports channels or a multi-room viewing package.',

    # --- Default Action ---
    'default': 'This is a stable customer. Send a Net Promoter Score (NPS) survey to gather feedback and make them feel valued.'
}

# Map for customers AT RISK of churning
churn_intervention_map = {
    # --- Cost & Tenure Drivers ---
    'MonthlyCharges': 'This customer\'s high monthly bill is a major issue. Review their plan immediately for discounts, or offer a service bundle that provides more value for a similar price.',
    'TotalCharges': 'Despite their spending history, this customer is a flight risk, suggesting a recent drop in perceived value. Offer a "tenure loyalty" bonus or a free service upgrade to show appreciation for their past business.',
    'tenure': 'This is a newer customer (low tenure) and is not yet "sticky." Engage them with a satisfaction check-in call and a guide to getting the most out of their services.',
    
    # --- Contract & Payment Drivers ---
    'Contract_Month-to-month': 'CRITICAL: This is the biggest churn indicator. Offer a 12 or 24-month contract with a significant signing bonus or a 10-15% discount to secure their loyalty.',
    'PaymentMethod_Electronic check': 'This manual payment method is inconvenient. Incentivize a switch to automatic credit card or bank payments with a one-time bill credit.',

    # --- Service & Engagement Drivers ---
    'InternetService_Fiber optic': 'While a premium service, its high cost may be driving churn. Offer a price lock guarantee for 12 months or check if a lower-cost tier still meets their needs.',
    'InternetService_DSL': 'This customer may be frustrated with internet speed. Run a line quality test and offer a promotional upgrade to a Fiber Optic plan.',
    'StreamingMovies_No': 'This customer is not engaged with our media services. Offer a 3-month free trial of the streaming package to increase service "stickiness".',
    'StreamingTV_No': 'This customer is not using our TV services. Offer a promotional bundle including the TV package at a low introductory rate.',

    # --- Default Action ---
    'default': 'This customer has a complex set of churn drivers. A manual review by a senior retention specialist is recommended.'
}

def get_churn_drivers(shap_values, feature_names, churn, top_n=3):
    """Identifies top features pushing a prediction towards churn."""
    feature_shap_map = dict(zip(feature_names, shap_values))
    # Filter for positive SHAP values (drivers of churn)
    churn_drivers = {k: v for k, v in feature_shap_map.items() if (churn and v > 0) or (not churn and v < 0)}
    # Sort by value, descending
    sorted_drivers = sorted(churn_drivers.items(), key=lambda item: item[1], reverse=churn)
    top_features = [feature[0] for feature in sorted_drivers[:top_n]]
    recommends_map = churn_intervention_map if churn else loyal_customer_map
    recomnends = list(set([recommends_map.get(f, recommends_map["default"]) for f in top_features]))
    return recomnends