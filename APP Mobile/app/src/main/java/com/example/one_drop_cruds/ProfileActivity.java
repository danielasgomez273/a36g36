package com.example.one_drop_cruds;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.example.one_drop_cruds.entities.DTOmedicalRecord;
import com.example.one_drop_cruds.entities.User;
import com.example.one_drop_cruds.utils.AdminSQLiteOpenHelper;
import com.example.one_drop_cruds.utils.UserSessionManager;

public class ProfileActivity extends AppCompatActivity {
    UserSessionManager userSessionManager;
    AdminSQLiteOpenHelper admin;
    EditText signup_name, signup_last_name, signup_age, signup_birth , signup_weight, signup_db_type, signup_db_therapy;
    Button edit_medical_data_button;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);

        admin = new AdminSQLiteOpenHelper(this, "bd_one_drop", null, 1); // version es para las futuras modificaciones de la estructura de la bd
        userSessionManager = new UserSessionManager(getApplicationContext());
        userSessionManager.validateLoguedUser(); // SI NO ESTA LOGUEADO, SE REDIRIGE A LOGIN

        signup_name = findViewById(R.id.signup_name);
        signup_last_name = findViewById(R.id.signup_last_name);
        signup_age = findViewById(R.id.signup_age);
        signup_birth = findViewById(R.id.signup_birth);
        signup_weight = findViewById(R.id.signup_weight);
        signup_db_type = findViewById(R.id.signup_db_type);
        signup_db_therapy = findViewById(R.id.signup_db_therapy);

        edit_medical_data_button = findViewById(R.id.edit_medical_data_button);

        setTextsForm();

    }
    public void setTextsForm(){
        DTOmedicalRecord medicalRecord = admin.getMedicalRecord(userSessionManager.getLoguedUsername());
        signup_name.setText(medicalRecord.getName().toString());
        signup_last_name.setText(medicalRecord.getLast_name().toString());
        signup_age.setText(medicalRecord.getAge().toString());
        signup_birth.setText(medicalRecord.getBirth().toString());
        signup_weight.setText(String.valueOf(medicalRecord.getWeight()));
        signup_db_type.setText(medicalRecord.getDbType().toString());
        signup_db_therapy.setText(medicalRecord.getDbTherapy().toString());
    }


    public void getTextsForm(){

    }
    public void updateFM(){
        getTextsForm();
    }



    public void toHome(View v){
        Intent home = new Intent(this, Home.class);
        startActivity(home);
    }
}