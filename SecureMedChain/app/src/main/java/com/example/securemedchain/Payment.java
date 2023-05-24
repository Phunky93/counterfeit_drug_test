package com.example.securemedchain;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
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

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class Payment extends AppCompatActivity
{
    TextView tv1;
    Button b1;
    EditText ed1,ed2;

    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_payment);

        SharedPreferences prefs = getSharedPreferences("userdetails", MODE_PRIVATE);
        String username=prefs.getString("username", "");

        tv1=(TextView)findViewById(R.id.m_id);
        ed1=(EditText)findViewById(R.id.q_want);
        ed2=(EditText)findViewById(R.id.private_key);

        String medicine_id = getIntent().getStringExtra("m_id");
        String medicine_name = getIntent().getStringExtra("med_name");
        String medicine_ingredients = getIntent().getStringExtra("ingredients");
        String medicine_exp_date = getIntent().getStringExtra("exp_date");
        String medicine_avail_quantity = getIntent().getStringExtra("avail_quantity");

        tv1.setText(medicine_id);

        b1=(Button) findViewById(R.id.pay);
        b1.setOnClickListener(new View.OnClickListener()
        {
            @Override
            public void onClick(View view)
            {
                String wanted_quantity=ed1.getText().toString();
                String private_key=ed2.getText().toString();

                    RequestQueue requestQueue= Volley.newRequestQueue(getApplicationContext());
                    StringRequest requ=new StringRequest(Request.Method.POST, "http://192.168.149.207:8000/do_payment/", new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {

                            Log.e("Response is: ", response.toString());
                            try {
                                JSONObject o = new JSONObject(response);
                                String dat = o.getString("msg");
                                if(dat.equals("yes"))
                                {
                                    Toast.makeText(Payment.this, "Payment done successfully!", Toast.LENGTH_LONG).show();
                                    Intent i1 = new Intent(Payment.this, User_home.class);
                                    startActivity(i1);
                                }
                                else if(dat.equals("Quantity not available"))
                                {
                                    Toast.makeText(Payment.this, "Quantity not available", Toast.LENGTH_LONG).show();
                                }
                                else
                                {
                                    Toast.makeText(Payment.this, "Error Happened!!!", Toast.LENGTH_LONG).show();
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

                            m.put("a_quantity", medicine_avail_quantity);
                            m.put("w_quantity",wanted_quantity);
                            m.put("m_id",medicine_id);
                            m.put("username",username);
                            m.put("private_key",private_key);


                            return m;
                        }

                    };
                    requestQueue.add(requ);


            }
        });


    }
}