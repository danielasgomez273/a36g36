package com.example.one_drop_cruds;

import static android.Manifest.permission.READ_EXTERNAL_STORAGE;
import static android.Manifest.permission.WRITE_EXTERNAL_STORAGE;

import androidx.activity.result.contract.ActivityResultContract;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.Manifest;
import android.annotation.SuppressLint;
import android.app.AlertDialog;
import android.content.ContentValues;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.graphics.Typeface;
import android.graphics.pdf.PdfDocument;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.os.Environment;
import android.provider.MediaStore;
import android.text.TextPaint;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.example.one_drop_cruds.utils.FilesManager;
import com.example.one_drop_cruds.utils.UserSessionManager;
import com.google.android.material.snackbar.Snackbar;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Home extends AppCompatActivity {
    UserSessionManager userSessionManager;
    TextView textView_welcome;
    FilesManager filesManager;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        textView_welcome = findViewById(R.id.textView_welcome);
        userSessionManager = new UserSessionManager(getApplicationContext());
        userSessionManager.validateLoguedUser(); // SI NO ESTA LOGUEADO, SE REDIRIGE A LOGIN
        textView_welcome.setText("¡¡ Bienvenido, "+userSessionManager.getLoguedUsername()+" !!");


        filesManager= new FilesManager(getApplicationContext(), this);
        this.askForPermissionsStorage();


        // Agrega el código para el botón "Volver a Inicio" que lleva a ContactoActivity
        /*
        Button backButton = findViewById(R.id.backButton);
        backButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), ContactoActivity.class);
                startActivity(intent);
            }
        });

         */
    }

    // METODOS DE NAVEGACION
    public void aRegistrarGlucemia(View v){
        Intent siguiente = new Intent(this, RegGlyActivity.class);
        startActivity(siguiente);
    }

    public void aRegistrarAnalisis(View v){
        Intent siguiente = new Intent(this, RegAnalysisActivity.class);
        startActivity(siguiente);
    }

    public void toWeight(View v){
        Intent weight = new Intent(this, RegWeightActivity.class);
        startActivity(weight);
    }

    public void toPressure(View v){
        Intent pressure = new Intent(this, RegPressureActivity.class);
        startActivity(pressure);
    }

    public void btn_export_data(View v){
        Bitmap bitmap = BitmapFactory.decodeResource(getResources(), R.drawable.onedrop); // solo para enviar logo de oneDrop a pdf
        if(/*filesManager.exportPdfFileReport(bitmap)*/ true){

            Log.i("TAG", "·······················································································································");
            Log.i("TAG", "HexportPdfFileReport");
            Log.i("TAG", "·······················································································································");

            Toast.makeText(this, "Se creo el PDF correctamente", Toast.LENGTH_LONG).show();
        } else {
            Toast.makeText(this, "Error en la creacion del PDF", Toast.LENGTH_LONG).show();
        }
    }



    /// PERMISOS FILES
    //askForPermissionsStorage y onRequestPermissionsResult deben ir en cada pagina que al cargar soliciten permiso a usuarios para acceder archivos
    public void askForPermissionsStorage() {
        if (Build.VERSION.SDK_INT > Build.VERSION_CODES.M) {
            // LA VERSION DE API ES MAYOR A 23, DEBEMOS PEDIR LOS PERMISOS EN TIEMPO DE EJECUCION
            Log.i("TAG", "API MAYOR A 23");
            if (ContextCompat.checkSelfPermission(Home.this, WRITE_EXTERNAL_STORAGE) == PackageManager.PERMISSION_GRANTED
                    && ContextCompat.checkSelfPermission(Home.this, READ_EXTERNAL_STORAGE) == PackageManager.PERMISSION_GRANTED) {
                // Return true si estan autorizados
                Log.i("TAG", "PERMISOS AUTORIZADOS!!!!!");
                //  this.createFile();
            } else {
                Log.i("TAG", "Permisos estaban rechazados... se los pido nuevamente");
                //pregunto si los permisos fueron rechazados anteriormente
                if (ActivityCompat.shouldShowRequestPermissionRationale(Home.this, WRITE_EXTERNAL_STORAGE)
                        && ActivityCompat.shouldShowRequestPermissionRationale(Home.this, READ_EXTERNAL_STORAGE)) {
                    Log.i("TAG", "El usuario previamente rechazo los permisos");
                } else {
                    Log.i("TAG", "lOS PERMIS NO ESTAN AUTORIZADOS PERO NO FUERON RECHAZADOS NUNCA..");
                }
                // voy a pedir permisos
                Log.i("TAG", "-------------- VOY A PEDIR LOS PERMISOS -------------");
                ActivityCompat.requestPermissions(Home.this, new String[]{WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE}, 200);
                Log.i("TAG", "-------------- VOY A PEDIR LOS PERMISOS -------------");
            }
        }
    }
    @SuppressLint("MissingSuperCall")
    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        if(requestCode == 200){
            if(grantResults.length >0 && grantResults[0] == PackageManager.PERMISSION_GRANTED && grantResults[1] == PackageManager.PERMISSION_GRANTED){
                Log.i("TAG","Permis autoo (onRequestPermissionsResult)!!!!!");
                Toast.makeText(Home.this,"Permis autoo (onRequestPermissionsResult)!", Toast.LENGTH_LONG).show();
                // this.createFile();
            } else{
                Log.i("TAG","El usuario previamente rechazo los permisos (onRequestPermissionsResult)");
                if(ActivityCompat.shouldShowRequestPermissionRationale(Home.this, WRITE_EXTERNAL_STORAGE)
                && ActivityCompat.shouldShowRequestPermissionRationale(Home.this, READ_EXTERNAL_STORAGE)){
                    // TRUE si el usuario nego los permisos, y coloco que no vuelva a ser mostrado el cartelito de solicitud
                    new AlertDialog.Builder(this).setMessage("Vos tenes que aceptar permis para usar la ap")
                            .setPositiveButton("Try again", new DialogInterface.OnClickListener() {
                                @Override
                                public void onClick(DialogInterface dialogInterface, int i) {
                                    // voy a pedir permisos
                                    Log.i("TAG","solicitando permisos nuevamente en dialog interface");
                                    ActivityCompat.requestPermissions(Home.this, new String[]{WRITE_EXTERNAL_STORAGE , READ_EXTERNAL_STORAGE}, 200);
                                }
                            })
                            .setNegativeButton("No gracias?", new DialogInterface.OnClickListener() {
                                @Override
                                public void onClick(DialogInterface dialogInterface, int i) {
                                    // salir?
                                    Log.i("TAG","Otra vez los permis siguen sin estar aceptados");
                                }
                            }).show();
                } else {
                    Log.i("TAG","TENES QUE HABILITAR PERMISOS MANUALMENTE");
                    Toast.makeText(Home.this,"TENES QUE HABILITAR PERMISOS MANUALMENTE", Toast.LENGTH_LONG).show();
                }
            }
        }
        super.onRequestPermissionsResult(requestCode,permissions,grantResults);
    }
}
