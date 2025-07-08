from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from config import connection_pool
from database import fetch_x, fetch_y
from app import best_fit, quadInterpolation, mean, median, mode

if not connection_pool:
    raise RuntimeError("Database connection pool is not initialized. Check your database configuration.")

@csrf_exempt
def get_analysis(request):
    if request.method == "POST":  # Change this to handle POST requests
        try:
            # Fetch x and y values for best fit line
            x_values = [x[0] for x in fetch_x()]
            y_values = [y[0] for y in fetch_y()]
            
            # Call the database functions
            mean_values = mean(x_values, y_values)
            median_values = median(x_values, y_values)
            mode_values = mode(x_values, y_values)
            
            # Calculate best fit line
            m, b = best_fit(x_values, y_values)

            # Calculate interpolation points
            interpolated_points = quadInterpolation(x_values, y_values)

            # Prepare the response
            response_data = {
                "mean": {"x": mean_values[0], "y": mean_values[1]},
                "median": {"x": median_values[0], "y": median_values[1]},
                "mode": {"x": mode_values[0], "y": mode_values[1]} if mode_values else "No mode",
                "bestFit": {"slope": m, "intercept": b},  # Include best fit line equation
                "interpolation": [{"x": x, "y": y} for x, y in interpolated_points],
                "x_values": x_values,
                "y_values": y_values,
            }

            return JsonResponse(response_data)
        except Exception as e:
            print(f"Error in get_analysis: {e}")
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)

@csrf_exempt
def handleCRUD(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(f"Received data: {data}")

            operation = data.get("operation")  # e.g., "create", "read", "update", "delete"
            metadata = data.get("metadata", {})

            changes = metadata.get("changes")

            # Process CRUD based on operation
            if operation == "create":
                # Handle creation logic
                x = changes.get("x")
                y = changes.get("y")
                try:
                    conn = connection_pool.getconn()
                    if conn:
                        print("connected")
                    cur = conn.cursor()
                    cur.execute("INSERT INTO datapoint (x_value, y_value) VALUES (%s, %s);", (x, y))
                    conn.commit()
                    cur.close()
                    connection_pool.putconn(conn)
                    print("Data point inserted successfully")
                    return JsonResponse({"success": True, "message": "Successfully inserted point"})
                except Exception as e:
                    print(f"Creation Error: {e}")
                    return JsonResponse({"error": "Insert Error"}, status=500)
            elif operation == "read":
                # Handle read logic
                pass
            elif operation == "update":
                # Handle update logic
                id = changes.get("id")
                x = changes.get("x")
                y = changes.get("y")
                try:
                    conn = connection_pool.getconn()
                    if conn:
                        print("connected")
                    cur = conn.cursor()
                    cur.execute(
                        "UPDATE datapoint SET x_value = %s, y_value = %s WHERE id = %s;",
                        (x, y, id),
                    )
                    conn.commit()
                    cur.close()
                    connection_pool.putconn(conn)
                    print("Data point updated successfully")
                    return JsonResponse({"success": True, "message": "Successfully updated point"})
                except Exception as e:
                    print(f"Update Error: {e}")
                    return JsonResponse({"error": "Update Error"}, status=500)

            elif operation == "delete":
                # Handle delete logic
                id = changes.get("id")
                print(f"Deleting data point with id: {id}")  # Debug log
                if not id:
                    return JsonResponse({"error": "ID is required for delete operation"}, status=400)
                try:
                    conn = connection_pool.getconn()
                    cur = conn.cursor()
                    cur.execute("DELETE FROM datapoint WHERE id = %s;", (id,))
                    conn.commit()
                    cur.close()
                    connection_pool.putconn(conn)
                    print("Data point deleted successfully")
                    return JsonResponse({"success": True, "message": "Successfully deleted point"})
                except Exception as e:
                    print(f"Delete Error: {e}")
                    return JsonResponse({"error": "Delete Error"}, status=500)
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({"error": "Invalid request"}, status=400)
    return JsonResponse({"error": "Invalid method"}, status=405)

@csrf_exempt
def get_data_points(request):
    if request.method == "GET":
        try:
            conn = connection_pool.getconn()
            cur = conn.cursor()
            cur.execute("SELECT id, x_value, y_value FROM datapoint")
            data_points = cur.fetchall()
            cur.close()
            connection_pool.putconn(conn)

            return JsonResponse(
                [{"id": row[0], "x_value": row[1], "y_value": row[2]} for row in data_points],
                safe=False
            )
        except Exception as e:
            print(f"Error fetching data points: {e}")
            return JsonResponse({"error": "Error fetching data points"}, status=500)
    return JsonResponse({"error": "Invalid method"}, status=405)
