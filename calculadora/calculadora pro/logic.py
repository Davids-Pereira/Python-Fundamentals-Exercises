import math

def calculate_expression(expression):
    try:
        clean_expr = expression.replace(' ', '')
        result = eval(clean_expr)
        
        if isinstance(result, float):
            return f"{round(result, 4)}"
        return str(result)
    
    except ZeroDivisionError:
        return "❌ Div/0"
    except Exception:
        return "⚠️ Error"

def calculate_sqrt(value_str):
    try:
        val = float(value_str)
        if val < 0:
            return "⛔ Negativo"
        return f"{round(math.sqrt(val), 4)}"
    except ValueError:
        return "⚠️ Error"