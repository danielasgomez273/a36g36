package com.example.one_drop_cruds;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;

import com.example.one_drop_cruds.utils.UserSessionManager;

public class Home extends AppCompatActivity {
    UserSessionManager userSessionManager;
    TextView textView_welcome;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);


        textView_welcome = findViewById(R.id.textView_welcome);
        userSessionManager = new UserSessionManager(getApplicationContext());
        userSessionManager.validateLoguedUser(); // SI NO ESTA LOGUEADO, SE REDIRIGE A LOGIN
        textView_welcome.setText("¡¡ Bienvenido, "+userSessionManager.getLoguedUsername()+" !!");
    }

    // METODOS DE NAVEGACION
    public void aRegistrarGlucemia(View v){
        Intent siguiente = new Intent(this, RegGlyActivity.class);
        startActivity(siguiente);
    }//

    public void aRegistrarAnalisis(View v){
        Intent siguiente = new Intent(this, RegAnalysisActivity.class);
        startActivity(siguiente);
    }//

    public void toWeight(View v){
        Intent weight = new Intent(this, RegWeightActivity.class);
        startActivity(weight);
    }
    public void toPressure(View v){
        Intent pressure = new Intent(this, RegPressureActivity.class);
        startActivity(pressure);
    }


    /////////////////////////////
}