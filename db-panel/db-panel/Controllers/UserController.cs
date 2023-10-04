using db_panel.Data;
using Microsoft.AspNetCore.Mvc;

namespace db_panel.Controllers
{
    public class UserController : Controller
    {
        ApplicationDbContext _context;
        public UserController(ApplicationDbContext context)
        {
            _context = context;
        }

        public IActionResult Index()
        {
            var users = _context.Users.ToList();
            return View(users);
        }
    }
}
