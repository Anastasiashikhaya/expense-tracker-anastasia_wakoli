from sqlalchemy.orm import Session
from models.expense import Expense
from datetime import datetime
import click

def get_expenses(db: Session, category: str = None, start_date: str = None, end_date: str = None):
    query = db.query(Expense)
    
    if category:
        query = query.filter(Expense.category == category)
    
    if start_date:
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        query = query.filter(Expense.date >= start_date)
    
    if end_date:
        end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
        query = query.filter(Expense.date <= end_date)
    
    return query.order_by(Expense.date.desc()).all()

@click.command()
@click.option('--category', help='Filter by category')
@click.option('--start-date', help='Start date for filtering (YYYY-MM-DD)')
@click.option('--end-date', help='End date for filtering (YYYY-MM-DD)')
def list_expenses_command(category, start_date, end_date):
    from db.database import SessionLocal
    db = SessionLocal()
    try:
        expenses = get_expenses(db, category, start_date, end_date)
        if not expenses:
            click.echo("No expenses found.")
            return
        
        for expense in expenses:
            click.echo(f"{expense.date} | {expense.category:15} | ${expense.amount:10.2f} | {expense.description or ''}")
    except Exception as e:
        click.echo(f"Error listing expenses: {str(e)}", err=True)
    finally:
        db.close()