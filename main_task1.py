from area_task1 import Circle, Triangle, calculate_area, is_right_angled

def main():
    print()
    
    try:
        radius = 5
        circle = Circle(radius)
        print(f"Площадь круга с радиусом {radius}: {calculate_area(circle):.2f}")
        print(f"Является ли круг прямоугольным? {'Да' if is_right_angled(circle) else 'Нет'}")
    except ValueError as e:
        print(f"Ошибка при создании круга: {e}")
    
    print()
    
    try:
        a, b, c = 3, 4, 5
        triangle = Triangle(a, b, c)
        print(f"Площадь треугольника со сторонами {a}, {b}, {c}: {calculate_area(triangle):.2f}")
        print(f"Является ли треугольник прямоугольным? {'Да' if is_right_angled(triangle) else 'Нет'}")
    except ValueError as e:
        print(f"Ошибка при создании треугольника: {e}")
    
    print()
    
    try:
        invalid_triangle = Triangle(1, 2, 5)
    except ValueError as e:
        print(f"ПОшибка, треугольник не может существовать: {e}")

if __name__ == "__main__":
    main()
