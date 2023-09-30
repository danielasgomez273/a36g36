package com.example.one_drop_cruds.utils;

import static android.Manifest.permission.READ_EXTERNAL_STORAGE;
import static android.Manifest.permission.WRITE_EXTERNAL_STORAGE;

import android.app.Activity;
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.graphics.Paint;
import android.graphics.Typeface;
import android.graphics.pdf.PdfDocument;
import android.os.Environment;
import android.text.TextPaint;
import android.widget.Toast;

import androidx.core.app.ActivityCompat;

import java.io.File;
import java.io.FileOutputStream;
import java.nio.file.Files;
import java.text.SimpleDateFormat;
import java.util.Date;

public class FilesManager {
    UserSessionManager userSessionManager;
    Context contex;
    Activity activity;
    public FilesManager(Context contex, Activity activity) {
        this.contex = contex;
        this.activity = activity;
        this.userSessionManager = new UserSessionManager(contex);
    }

    private String getLoguedUsername(){
       return userSessionManager.getLoguedUsername();
    }
    private String createUniqueFileName(){
        String now = new SimpleDateFormat("dd-MM-yyyy").format(new Date());
        return "Reporte ONE DROP - "+getLoguedUsername()+" - "+now+".pdf";
    }

    private String getAllRegisters(){
        String result = "Sin resultados \n";


                /*
                "Lorem Ipsum is simply dummy text of the printing and typesetting industry. \n" +
                "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, \n" +
                "when an unknown printer took a galley of type and scrambled it to make a type specimen book. \n" +
                "It has survived not only five centuries, but also the leap into electronic typesetting, \n" +
                "remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset\n" +
                " sheets containing Lorem Ipsum passages, and more recently with desktop publishing software\n" +
                " like Aldus PageMaker including versions of Lorem Ipsum.\n";

                 */
        return result;
    }

    public boolean exportPdfFileReport(Bitmap bitmap) {
        Boolean exportSuccess = false;
        String docTitle = "Reportes generados con fecha: "+new SimpleDateFormat("dd/MM/yyyy").format(new Date());

        String descriptionText = getAllRegisters();


        PdfDocument pdfDocument = new PdfDocument();
        Paint paint = new Paint();
        TextPaint title = new TextPaint();
        TextPaint description = new TextPaint();

        PdfDocument.PageInfo pageInfo = new PdfDocument.PageInfo.Builder(816, 1054, 1).create();
        PdfDocument.Page page = pdfDocument.startPage(pageInfo);

        // DEBERIA VER LA FORMA DE OBTENER ESTOS DATOS DESDE ESTA CLASE Y NO ENVIANDOLOS POR PARAMETROOOOO
        // DEBERIA VER LA FORMA DE OBTENER ESTOS DATOS DESDE ESTA CLASE Y NO ENVIANDOLOS POR PARAMETROOOOO
        // DEBERIA VER LA FORMA DE OBTENER ESTOS DATOS DESDE ESTA CLASE Y NO ENVIANDOLOS POR PARAMETROOOOO
        // DEBERIA VER LA FORMA DE OBTENER ESTOS DATOS DESDE ESTA CLASE Y NO ENVIANDOLOS POR PARAMETROOOOO
        // DEBERIA VER LA FORMA DE OBTENER ESTOS DATOS DESDE ESTA CLASE Y NO ENVIANDOLOS POR PARAMETROOOOO

        // Bitmap bitmap, bitmapEscala;
        // bitmap = BitmapFactory.decodeResource(AppCompactActivity.getResources(), R.drawable.logo);
        Bitmap bitmapScale = Bitmap.createScaledBitmap(bitmap, 80, 80, false);
        Canvas canvas = page.getCanvas();
        canvas.drawBitmap(bitmapScale, 368, 20, paint);


        title.setTypeface(Typeface.create(Typeface.DEFAULT, Typeface.BOLD));
        title.setTextSize(20);
        canvas.drawText(docTitle, 10, 150, title);

        description.setTypeface(Typeface.defaultFromStyle(Typeface.NORMAL));
        description.setTextSize(14);

        String[] arrayDescription = descriptionText.split("\n");
        int y = 200;
        for (int i = 0; i < arrayDescription.length; i++) {
            canvas.drawText(arrayDescription[i], 10, y, description);
            y += 15;
        }
        pdfDocument.finishPage(page);

        File file = new File(Environment.getExternalStoragePublicDirectory(Environment.DIRECTORY_DOWNLOADS), createUniqueFileName());
        try {
            pdfDocument.writeTo(new FileOutputStream(file));
            exportSuccess = true;
        } catch (Exception e) {
            e.printStackTrace();
        }
        pdfDocument.close();
        return exportSuccess;
    }


}
