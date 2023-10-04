using db_panel.Models;
using Microsoft.EntityFrameworkCore;

namespace db_panel.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions options) : base(options)
        {
        }
        public DbSet<User> Users { get; set; }
    }
}
