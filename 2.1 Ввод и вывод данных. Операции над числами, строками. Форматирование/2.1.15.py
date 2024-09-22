def main():
    hours, minutes, T = int(input()), int(input()), int(input())
    time = hours * 60 + minutes
    few_hours = str(((time + T) // 60) % 24)
    few_minutes = str((time + T) % 60)
    if len(few_hours) == 1:
        few_hours = '0' + few_hours
    if len(few_minutes) == 1:
        few_minutes = '0' + few_minutes
    print(f'{few_hours}:{few_minutes}')

if __name__ == "__main__":
    main()