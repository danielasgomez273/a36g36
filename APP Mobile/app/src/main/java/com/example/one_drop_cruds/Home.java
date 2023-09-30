package com.example.one_drop_cruds;

import static android.Manifest.permission.READ_EXTERNAL_STORAGE;
import static android.Manifest.permission.WRITE_EXTERNAL_STORAGE;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.graphics.Typeface;
import android.graphics.pdf.PdfDocument;
import android.os.Bundle;
import android.os.Environment;
import android.text.TextPaint;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.example.one_drop_cruds.utils.FilesManager;
import com.example.one_drop_cruds.utils.UserSessionManager;

import java.io.File;
import java.io.FileOutputStream;
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

        filesManager = new FilesManager(getApplicationContext(), this);

        // Agrega el código para el botón "Volver a Inicio" que lleva a ContactoActivity
        Button backButton = findViewById(R.id.backButton);
        backButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(getApplicationContext(), ContactoActivity.class);
                startActivity(intent);
            }
        });
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

    // PERMISOS
    private boolean checkPermission() {
        int writePermission = ContextCompat.checkSelfPermission(this, WRITE_EXTERNAL_STORAGE);
        int readPermission = ContextCompat.checkSelfPermission(this, READ_EXTERNAL_STORAGE);
        return writePermission == PackageManager.PERMISSION_GRANTED && readPermission == PackageManager.PERMISSION_GRANTED;
    }

    private void requestPermissions() {
        ActivityCompat.requestPermissions(this, new String[]{WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE}, 200);
    }

    @SuppressLint("MissingSuperCall")
    @Override
    public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        if(requestCode == 200) {
            if(grantResults.length > 0) {
                boolean writeStorage = grantResults[0] == PackageManager.PERMISSION_GRANTED;
                boolean readStorage = grantResults[1] == PackageManager.PERMISSION_GRANTED;
                if(writeStorage && readStorage) {
                    Toast.makeText(this, "Permiso concedido", Toast.LENGTH_LONG).show();
                } else {
                    Toast.makeText(this, "Permiso denegado", Toast.LENGTH_LONG).show();
                }
            }
        }
    }

    // CREAR PDF
    public void btn_export_data(View v) {
        // Verifica los permisos antes de crear el archivo PDF
        if (checkPermission()) {
            createFile();
        } else {
            requestPermissions();
        }
    }

    private String createUniqueName() {
        String now = new SimpleDateFormat("yyyyMMdd_HHmmss").format(new Date());
        return "PDF_"+now+".pdf";
    }

    public void createFile() {
        String tituloText = "Este es el titulo del documento";
        String descripcionText = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. \n" +
                "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, \n" +
                "when an unknown printer took a galley of type and scrambled it to make a type specimen book. \n" +
                "It has survived not only five centuries, but also the leap into electronic typesetting, \n" +
                "remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset\n" +
                "sheets containing Lorem Ipsum passages, and more recently with desktop publishing software\n" +
                "like Aldus PageMaker including versions of Lorem Ipsum.\n";

        PdfDocument pdfDocument = new PdfDocument();
        Paint paint = new Paint();
        TextPaint titulo = new TextPaint();
        TextPaint descripcion = new TextPaint();

        PdfDocument.PageInfo pageInfo = new PdfDocument.PageInfo.Builder(816, 1054, 1).create();
        PdfDocument.Page page = pdfDocument.startPage(pageInfo);
        Canvas canvas = page.getCanvas();

        titulo.setTypeface(Typeface.create(Typeface.DEFAULT, Typeface.BOLD));
        titulo.setTextSize(20);
        canvas.drawText(tituloText, 10, 150, titulo);

        descripcion.setTypeface(Typeface.defaultFromStyle(Typeface.NORMAL));
        descripcion.setTextSize(14);

        String[] arrDescripcion = descripcionText.split("\n");
        int y = 200;
        for (int i = 0; i < arrDescripcion.length; i++) {
            canvas.drawText(arrDescripcion[i], 10, y, descripcion);
            y += 15;
        }

        pdfDocument.finishPage(page);

        File file = new File(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS), createUniqueName());
        try {
            pdfDocument.writeTo(new FileOutputStream(file));
            Toast.makeText(this, "Se creó el PDF correctamente", Toast.LENGTH_LONG).show();
        } catch (Exception e) {
            Toast.makeText(this, "Error al crear el PDF: " + e.getMessage(), Toast.LENGTH_LONG).show();
            e.printStackTrace();
        }
        pdfDocument.close();
    }
}
