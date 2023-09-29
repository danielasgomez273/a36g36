package com.example.one_drop_cruds.utils;


import android.content.Context;
import android.content.Intent;

import com.example.one_drop_cruds.UserLoginActivity;

public class UserSessionManager {
    Context context;
    SharedPrefManager sharedPrefManager;
    public UserSessionManager(Context context) {
        this.context = context;
        this.sharedPrefManager = new SharedPrefManager(context , "oneDrop_shared_preferences");
    }
    public void validateLoguedUser(){
        if(this.getLoguedUsername() == null){
            this.context.startActivity(new Intent(this.context, UserLoginActivity.class));
        }
    }
    public String getLoguedUsername(){
        return sharedPrefManager.getString("logued_username", null);
    }
}
