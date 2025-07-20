from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from models.expense import Expense
import click

def get_summary(db: Session, month: str = None, year: int = None):
    query = db.query(
        Expense.category,
        func.sum(Expense.amount).label('total')
    ).group_by(Expense.category)
    
    if month:
        query = query.filter(Expense.date.like(f"%-{month}-%"))
    
    if year:
        query = query.filter(extract('year', Expense.date) == year)
    
    return query.order_by(func.sum(Expense.amount).desc()).all()

@click.command()
@click.option('--month', help='Month to summarize (e.g., "07" for July)')
@click.option('--year', type=int, help='Year to summarize')
def summary_command(month, year):
    from db.database import SessionLocal
    db = SessionLocal()
    try:
        summary = get_summary(db, month, year)
        if not summary:
            click.echo("No expenses found for the given criteria.")
            return
        
        click.echo("Expense Summary:")
        click.echo("----------------")
        total = 0
        for category, amount in summary:
            click.echo(f"{category:15}: ${amount:.2f}")
            total += amount
        
        click.echo("----------------")
        click.echo(f"Total: ${total:.2f}")
    except Exception as e:
        click.echo(f"Error generating summary: {str(e)}", err=True)
    finally:
        db.close()