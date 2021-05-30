# Solution of;
# Project Euler Problem 1: Multiples of 3 and 5
# https://projecteuler.net/problem=1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
#
# by lcsm29 http://github.com/lcsm29/project-euler
class Rb0001
    def inject(num)
      (0...num).select { |i| (i % 3).zero? || (i % 5).zero? }.inject(0) { |i, sum| sum + i }
    end
  
    def reduce(num)
      (0...num).select { |i| (i % 3).zero? || (i % 5).zero? }.reduce(:+)
    end
  
    def triple_sum(num)
      n = {}
      [3, 5, 15].each do |i| 
        if num % i != 0
          n[i] = num
        else 
          n[i] = num - 1
        end
      end
      3.step(n[3], 3).sum + 5.step(n[5], 5).sum - 15.step(n[15], 15).sum
    end
  
    def gauss_sum(num)
      n_mults = {}
      result = {}
      [3, 5, 15].each do |i| 
        if num % i != 0
          n_mults[i] = num / i
        else 
          n_mults[i] = num / i - 1
        end
        result[i] = i * 0.5 * n_mults[i] * (n_mults[i] + 1)
      end
      (result[3] + result[5] - result[15]).to_i
    end
  end
  
  def caller(obj, fn_names, n, num_iterations)
    elapsed = {}
    fn_names.each do |fn|
      each_runs = []
      outer_start = Time.now
      (0...num_iterations).each do |_|
        start = Time.now
        obj.send(fn, n)
        finished = Time.now
        each_runs.append((finished - start) * 10**9)
      end
      outer_finished = Time.now
      outer_elapsed = ((outer_finished - outer_start) * 10**9).to_i.to_s.reverse.gsub(/(\d{3})(?=\d)/, '\\1,').reverse
      result = obj.send(fn, n)
      elapsed[fn] = outer_elapsed, each_runs.min, each_runs.inject(:+) / each_runs.length, each_runs.max, result
    end
    elapsed
  end
  
  def main
    n = 1000
    n_iters = 2500
    ans = 233168
    obj = Rb0001.new
    fn_names = 'inject', 'reduce', 'triple_sum', 'gauss_sum'
    results = caller(obj, fn_names, n, n_iters)
    fastest_avg = Float::INFINITY
    num_failed = 0
    results.each do |k, v|
      print "time elapsed #{k}: #{v[0]}ns (min #{v[1].to_i}ns, avg #{v[2].to_i}ns, max #{v[3].to_i}ns) "
      fastest_avg = [fastest_avg, v[2]].min
      if v[4] != ans
        print "Expected result: #{ans}, Actual result: #{v[4]}\r\n"
        num_failed += 1
      else puts end
    end
    {'fastest_avg': fastest_avg, 'n_iter': n_iters.to_i, 'num_failed': num_failed}
  end
  main
  