package com.example.one_drop_cruds;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

import com.example.one_drop_cruds.entities.DTOmedicalRecord;
import com.example.one_drop_cruds.entities.User;
import com.example.one_drop_cruds.utils.AdminSQLiteOpenHelper;
import com.example.one_drop_cruds.utils.UserSessionManager;

public class ProfileActivity extends AppCompatActivity {
    UserSessionManager userSessionManager;
    AdminSQLiteOpenHelper admin;
    EditText signup_name, signup_last_name, signup_age, signup_birth, signup_weight, signup_db_type, signup_db_therapy;
    Button edit_medical_data_button, selectImageButton;
    ImageView profileImage;
    private static final int PICK_IMAGE = 100;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_profile);

        admin = new AdminSQLiteOpenHelper(this, "bd_one_drop", null, 1);
        userSessionManager = new UserSessionManager(getApplicationContext());
        userSessionManager.validateLoguedUser();

        signup_name = findViewById(R.id.signup_name);
        signup_last_name = findViewById(R.id.signup_last_name);
        signup_age = findViewById(R.id.signup_age);
        signup_birth = findViewById(R.id.signup_birth);
        signup_weight = findViewById(R.id.signup_weight);
        signup_db_type = findViewById(R.id.signup_db_type);
        signup_db_therapy = findViewById(R.id.signup_db_therapy);
        edit_medical_data_button = findViewById(R.id.edit_medical_data_button);
        selectImageButton = findViewById(R.id.selectImageButton);
        profileImage = findViewById(R.id.profile_image);

        setTextsForm();

        selectImageButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                openGallery();
            }
        });
    }

    private void openGallery() {
        Intent gallery = new Intent(Intent.ACTION_PICK, android.provider.MediaStore.Images.Media.INTERNAL_CONTENT_URI);
        startActivityForResult(gallery, PICK_IMAGE);
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        super.onActivityResult(requestCode, resultCode, data);

        if (resultCode == RESULT_OK && requestCode == PICK_IMAGE) {
            Uri imageUri = data.getData();
            profileImage.setImageURI(imageUri);
        }
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