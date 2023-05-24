package com.example.securemedchain;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.Bundle;
import android.util.Base64;
import android.util.Log;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.AuthFailureError;
import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.google.android.material.navigation.NavigationView;
import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class Scan_Page extends AppCompatActivity implements View.OnClickListener{
    Button scanBtn,b1;
    TextView messageText;
    NavigationView navigationView;
    String get_username;
    String hash_value;
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_scan_page);

        SharedPreferences prefs = getSharedPreferences("userdetails", MODE_PRIVATE);
        String username=prefs.getString("username", "");
        get_username=username;
        b1=(Button)findViewById(R.id.get_med_info);
        scanBtn = (Button) findViewById(R.id.scanBtn);
        messageText = findViewById(R.id.textContent);


        // adding listener to the button
        scanBtn.setOnClickListener(this);

        b1.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
                RequestQueue requestQueue= Volley.newRequestQueue(getApplicationContext());
                StringRequest requ=new StringRequest(Request.Method.POST, "http://192.168.149.207:8000/get_info/", new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

                        Log.e("Response is: ", response.toString());
                        try {
                            JSONObject o = new JSONObject(response);
                            JSONArray jsonArray = o.getJSONArray("data");
                            for (int i=0;i<jsonArray.length();i++){
                                JSONObject result = jsonArray.getJSONObject(i);
                                Log.e("result", String.valueOf(result));
                                String m_id=result.getString("m_id");
                                String med_name=result.getString("med_name");
                                String ingredients=result.getString("ingredients");
                                String exp_date=result.getString("exp_date");
                                String avail_quantity=result.getString("avail_quantity");

                                Log.e("med_name : ",med_name);
                                Log.e("ingredients : ",ingredients);
                                Log.e("exp_date : ",exp_date);
                                Log.e("avail_quantity : ",avail_quantity);

                                Intent intent = new Intent(Scan_Page.this, Medicine_info.class);
                                intent.putExtra("m_id", m_id);
                                intent.putExtra("med_name", med_name);
                                intent.putExtra("ingredients", ingredients);
                                intent.putExtra("exp_date", exp_date);
                                intent.putExtra("avail_quantity", avail_quantity);
                                startActivity(intent);

                            }
                        }
                        catch (Exception e){
                            e.printStackTrace();

                        }

                    }
                }, new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
//                Log.e(TAG,error.getMessage());
                        error.printStackTrace();
                    }
                }){
                    @Override
                    protected Map<String, String> getParams() throws AuthFailureError {
                        Map<String,String> m=new HashMap<>();
                        m.put("value", hash_value);
                        m.put("username",get_username);

                        return m;
                    }

                };
                requestQueue.add(requ);
            }
        });

    }
    @Override
    public void onClick(View v) {
        // we need to create the object
        // of IntentIntegrator class
        // which is the class of QR library
        IntentIntegrator intentIntegrator = new IntentIntegrator(this);
        intentIntegrator.setPrompt("Scan a barcode or QR Code");
        intentIntegrator.setOrientationLocked(true);
        intentIntegrator.initiateScan();
    }
    @Override
    protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
        super.onActivityResult(requestCode, resultCode, data);
        IntentResult intentResult = IntentIntegrator.parseActivityResult(requestCode, resultCode, data);
        // if the intentResult is null then
        // toast a message as "cancelled"
        if (intentResult != null)
        {
            if (intentResult.getContents() == null)
            {
                Toast.makeText(getBaseContext(), "Cancelled", Toast.LENGTH_SHORT).show();
            } else
            {
                // if the intentResult is not null we'll set
                // the content and format of scan message
                hash_value=intentResult.getContents();
                messageText.setText(intentResult.getContents());

            }
        }
        else
        {
            super.onActivityResult(requestCode, resultCode, data);
        }
    }


}