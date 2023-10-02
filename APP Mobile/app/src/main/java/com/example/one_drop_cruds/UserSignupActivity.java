package com.example.one_drop_cruds;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;
import com.example.one_drop_cruds.databinding.ActivityUserSignupBinding;
import com.example.one_drop_cruds.utils.AdminSQLiteOpenHelper;
import com.example.one_drop_cruds.utils.SharedPrefManager;

public class UserSignupActivity extends AppCompatActivity {
    SharedPrefManager sharedPrefManager;
    ActivityUserSignupBinding binding;
    AdminSQLiteOpenHelper adminBD;
    EditText signup_email, signup_password , signup_confirm;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityUserSignupBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        adminBD = new AdminSQLiteOpenHelper(this, "bd_one_drop", null, 1); // version es para las futuras modificaciones de la estructura de la bd
        sharedPrefManager = new SharedPrefManager(getApplicationContext() , "oneDrop_shared_preferences");

        signup_email = findViewById(R.id.signup_email);
        signup_password = findViewById(R.id.signup_password);
        signup_confirm = findViewById(R.id.signup_confirm);

    }
    public void toLogin(View v){
        Intent intent = new Intent(UserSignupActivity.this, UserLoginActivity.class);
        startActivity(intent);
    }
    public void signupUser(View v){
        String email = signup_email.getText().toString();
        String password = signup_password.getText().toString();
        String confirmPassword = signup_confirm.getText().toString();

        if(email.equals("")||password.equals("")||confirmPassword.equals(""))
            Toast.makeText(UserSignupActivity.this, "¡ Debes completar todos los campos !", Toast.LENGTH_SHORT).show();
        else{
            if(password.equals(confirmPassword)){
                Boolean checkUserEmail = adminBD.checkEmail(email);
                if(!checkUserEmail){
                    Boolean insert = adminBD.createUser(email, password);
                    if(insert){
                        Toast.makeText(UserSignupActivity.this, "¡Registro exitoso!", Toast.LENGTH_SHORT).show();
                        sharedPrefManager.setLoguedUser(email);
                        Intent intent = new Intent(getApplicationContext(), UserMedicalData.class);
                        startActivity(intent);
                    }else{
                        Toast.makeText(UserSignupActivity.this, "Error durante el registro!", Toast.LENGTH_SHORT).show();
                    }
                }
                else{
                    Toast.makeText(UserSignupActivity.this, "Ya estas registrado!", Toast.LENGTH_SHORT).show();
                    Intent intent = new Intent(getApplicationContext(), UserLoginActivity.class);
                    startActivity(intent);
                }
            }else{
                Toast.makeText(UserSignupActivity.this, "Las contraseñas no concuerdan!", Toast.LENGTH_SHORT).show();
            }
        }
    }



}