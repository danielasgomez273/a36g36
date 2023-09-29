package com.example.one_drop_cruds.utils;

import android.content.Context;
import android.content.SharedPreferences;

public class SharedPrefManager {
    private Context context;
    private SharedPreferences sharedPref;
    private SharedPreferences.Editor  sharedPrefEditor;
    public SharedPrefManager(Context context , String preferenceName ) {
        this.context = context; //Obtengo el contexto de la aplicacion, y sobre el llamo a get shared pref
        this.sharedPref = context.getSharedPreferences(preferenceName, Context.MODE_PRIVATE);  //Creo una archivo shared preference con el nombre "preferenceName" y con acceso privado
        this.sharedPrefEditor = this.sharedPref.edit(); //CREO UN EDITOR PARA PODER AGREGAR DATOS
    }

    public void setLoguedUser(String username){
        this.sharedPrefEditor.putString("logued_username", username);
        // revisar otros datos que queremos guardar para almacenar de user
        // revisar otros datos que queremos guardar para almacenar de user
        // revisar otros datos que queremos guardar para almacenar de user
        // revisar otros datos que queremos guardar para almacenar de user
        // revisar otros datos que queremos guardar para almacenar de user

        sharedPrefEditor.apply(); // EJECUTA CAMBIOS de forma ASINCRONA!
    }
    public void setString(String key, String value){
        this.sharedPrefEditor.putString(key ,value); // AGREGO CLAVE Y VALOR
        sharedPrefEditor.apply(); // EJECUTA CAMBIOS de forma ASINCRONA!
    }
    public void setInt(String key, Integer value){
        this.sharedPrefEditor.putInt(key ,value);
        sharedPrefEditor.apply(); // EJECUTA CAMBIOS de forma ASINCRONA!
    }
    public void setFloat(String key, Float value){
        this.sharedPrefEditor.putFloat(key ,value);
        sharedPrefEditor.apply(); // EJECUTA CAMBIOS de forma ASINCRONA!
    }
    public void setBoolean(String key, Boolean value){
        this.sharedPrefEditor.putBoolean(key ,value);
        sharedPrefEditor.apply(); // EJECUTA CAMBIOS de forma ASINCRONA!
    }
    public String getString(String key, String defaultValue){
        return this.sharedPref.getString(key, defaultValue);
    }
    public Float getFloat(String key, Float defaultValue){
        return this.sharedPref.getFloat(key, defaultValue);
    }
    public Integer getInt(String key, Integer defaultValue){
        return this.sharedPref.getInt(key, defaultValue);
    }
    public Boolean getBoolean(String key, Boolean defaultValue){
        return this.sharedPref.getBoolean(key, defaultValue);
    }
    public void clearSharedPref(){
        sharedPref.edit().clear().apply();
    }
}
