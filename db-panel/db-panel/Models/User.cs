using System.ComponentModel.DataAnnotations;

namespace db_panel.Models
{
    public class User
    {
        public int UserId { get; set; }
        [Required]
        public string? Name { get; set; }
        [Required]
        public string? Email { get; set; }
    }
}
