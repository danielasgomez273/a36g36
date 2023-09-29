package com.example.one_drop_cruds;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;
import com.example.one_drop_cruds.databinding.ActivityUserLoginBinding;
import com.example.one_drop_cruds.utils.AdminSQLiteOpenHelper;
import com.example.one_drop_cruds.utils.SharedPrefManager;

public class UserLoginActivity extends AppCompatActivity {
    SharedPrefManager sharedPrefManager;
    ActivityUserLoginBinding binding;
    AdminSQLiteOpenHelper adminBD;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityUserLoginBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        adminBD = new AdminSQLiteOpenHelper(this, "bd_one_drop", null, 1); // version es para las futuras modificaciones de la estructura de la bd
        sharedPrefManager = new SharedPrefManager(getApplicationContext() , "oneDrop_shared_preferences");
        binding.loginButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String email = binding.loginEmail.getText().toString();
                String password = binding.loginPassword.getText().toString();

                if(email.equals("")||password.equals(""))
                    Toast.makeText(UserLoginActivity.this, "Debes completar todos los campos", Toast.LENGTH_SHORT).show();
                else{
                    Boolean checkCredentials = adminBD.checkEmailPassword(email, password);

                    if(checkCredentials){
                        sharedPrefManager.setLoguedUser(email);
                        Toast.makeText(UserLoginActivity.this, "Login exitoso!", Toast.LENGTH_SHORT).show();
                        Intent intent  = new Intent(getApplicationContext(), Home.class);
                        startActivity(intent);
                    }else{
                        Toast.makeText(UserLoginActivity.this, "¡ Credenciales erroneas !", Toast.LENGTH_SHORT).show();
                    }
                }
            }
        });

        binding.signupRedirectText.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(UserLoginActivity.this, UserSignupActivity.class);
                startActivity(intent);
            }
        });
    }
}