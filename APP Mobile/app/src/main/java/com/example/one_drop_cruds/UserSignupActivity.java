package com.example.one_drop_cruds;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;
import com.example.one_drop_cruds.databinding.ActivityUserSignupBinding;
import com.example.one_drop_cruds.utils.AdminSQLiteOpenHelper;

public class UserSignupActivity extends AppCompatActivity {

    ActivityUserSignupBinding binding;
    // DatabaseHelper databaseHelper;
    AdminSQLiteOpenHelper adminBD;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityUserSignupBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        adminBD = new AdminSQLiteOpenHelper(this, "bd_one_drop", null, 1); // version es para las futuras modificaciones de la estructura de la bd


        binding.signupButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String email = binding.signupEmail.getText().toString();
                String password = binding.signupPassword.getText().toString();
                String confirmPassword = binding.signupConfirm.getText().toString();

                if(email.equals("")||password.equals("")||confirmPassword.equals(""))
                    Toast.makeText(UserSignupActivity.this, "¡ Debes completar todos los campos !", Toast.LENGTH_SHORT).show();
                else{
                    if(password.equals(confirmPassword)){
                        Boolean checkUserEmail = adminBD.checkEmail(email);

                        if(!checkUserEmail){
                            Boolean insert = adminBD.createUser(email, password);

                            System.out.println("********************************************************************");
                            System.out.println("REGISTRO DE USUARIO EXITOSO!");
                            System.out.println("********************************************************************");

                            Toast.makeText(UserSignupActivity.this, "¡Registro exitoso!", Toast.LENGTH_SHORT).show();
                            if(insert){
                                // Toast.makeText(UserSignupActivity.this, "¡Registro exitoso!", Toast.LENGTH_SHORT).show();


                                // ACA DEBEMOS
                                // AGREGAR USUARIO A SHARED PREFERNECES
                                // REDIRIGIR A FORMULARIO DE AGREGAR DATOS MEDICOS? O A HOME...
                                Intent intent = new Intent(getApplicationContext(), UserLoginActivity.class);
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
        });

        binding.loginRedirectText.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(UserSignupActivity.this, UserLoginActivity.class);
                startActivity(intent);
            }
        });

    }
}